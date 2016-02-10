import sys
import logging
import subprocess
from ophyd import AreaDetector
from ophyd.areadetector.plugins import (PluginBase, get_areadetector_plugin,
                                        ProcessPlugin)


class DetectorNode:
    def __init__(self, det, port_name):
        self.plugin = det
        self.port_name = port_name
        self.children = []

    def __repr__(self):
        # hack because I don't have the proper prefix yet
        return '{}(port_name={!r})'.format(self.plugin.__class__.__name__,
                                           self.port_name)


class PluginNode:
    def __init__(self, plugin, parent=None):
        self.plugin = plugin
        self.parent = parent
        self.children = []

    @property
    def port_name(self):
        return self.plugin.port_name.get()

    def __repr__(self):
        return '{}(port_name={!r})'.format(self.plugin.__class__.__name__,
                                           self.port_name)


class PluginTree:
    def __init__(self):
        self.roots = []
        self.source_ports = {}
        self.port_to_plugin = {}
        self.waiting = {}  # waiting for parent :(

    def done(self):
        # assume all waiting nodes are top-level detectors
        for port_name, children in self.waiting.items():
            parent = DetectorNode(AreaDetector('todo', name=port_name), port_name)
            for child_plugin in children:
                child_plugin.parent = parent
                parent.children.append(child_plugin)
            self.roots.append(parent)

        self.waiting = {}

    def get_paths(self):
        def iter_children(plugin, parent_nodes):
            if not plugin.children:
                yield parent_nodes
            else:
                for child in plugin.children:
                    yield from iter_children(child, parent_nodes + [child])

        for plugin in self.top_level:
            for path in iter_children(plugin, [plugin]):
                yield [node.plugin for node in path]

    @property
    def top_level(self):
        for port_name, plugin in self.waiting.items():
            yield from plugin

        for plugin in self.roots:
            yield plugin

    def __iter__(self):
        def iter_children(plugin):
            yield plugin
            for plugin in plugin.children:
                yield from iter_children(plugin)

        for plugin in self.top_level:
            yield from iter_children(plugin)

    def add(self, plugin):
        port_name = plugin.port_name.get()
        if port_name is None:
            raise ValueError('Plugin not connected')

        node = PluginNode(plugin)
        self.port_to_plugin[port_name] = node

        if port_name in self.waiting:
            for child_plugin in self.waiting[port_name]:
                child_plugin.parent = node
                node.children.append(child_plugin)
            del self.waiting[port_name]

        source_port = plugin.nd_array_port.get()
        self.source_ports[plugin] = source_port

        try:
            parent = self.port_to_plugin[source_port]
        except KeyError:
            if source_port not in self.waiting:
                self.waiting[source_port] = []

            self.waiting[source_port].append(node)
        else:
            parent.children.append(node)
            node.parent = parent


def grep_pvs(prefix, path='/cf-update/*.dbl', suffix='EnableCallbacks',
             grep_tool='/bin/grep', ignore_exceptions=True):
    expr = '^{}.*{}$'.format(prefix, suffix)
    command = '{} -he "{}" {}'.format(grep_tool, expr, path)

    try:
        stdout = subprocess.check_output(command, stderr=subprocess.DEVNULL, shell=True)
    except subprocess.CalledProcessError as ex:
        # some permissions errors in /cf-update
        if not ignore_exceptions:
            raise
        stdout = ex.output

    stdout = stdout.decode('ascii')
    for match in stdout.split('\n'):
        match = match.strip()
        if match:
            yield match[:-len(suffix)]


def get_plugins_by_prefix(det_prefix, verbose=True):
    for prefix in grep_pvs(det_prefix):
        try:
            # Try to guess the plugin-type by regular expression
            plugin = get_areadetector_plugin(prefix)
        except ValueError:
            # Or give up and just give a generic plugin
            plugin = PluginBase(prefix)
        else:
            plugin._name = plugin.port_name.get()
            yield plugin


def make_port_tree(plugins):
    tree = PluginTree()
    for plugin in plugins:
        tree.add(plugin)
    return tree


def check_plugin(plugin):
    blocking = plugin.blocking_callbacks.get()
    if blocking:
        yield ('Blocking', plugin.blocking_callbacks)

        min_time = plugin.min_callback_time.get()
        if blocking and min_time > 0:
            yield ('Minimum time set', plugin.min_time)

    if (isinstance(plugin, ProcessPlugin) and plugin.enable_filter.get()):
        yield ('Filter is enabled', plugin.enable_filter)

        n_filter = plugin.num_filter.get()
        cb_filter = plugin.filter_callbacks.get(as_string=True)
        if n_filter > 0 and cb_filter == 'Array N only':
            yield ('Only processing 1 callback per {} images'
                   ''.format(n_filter), plugin.num_filter)


def sup_ad(prefix):
    plugins = list(get_plugins_by_prefix(prefix))
    for plugin in plugins:
        port = plugin.port_name.get()
        source_port = plugin.nd_array_port.get()
        print('Plugin: {} Port: {!r} Source: {!r}'
              ''.format(plugin, port, source_port))

    plugin_map = make_port_tree(plugins)
    plugin_map.done()
    for i, path in enumerate(plugin_map.get_paths()):
        print('- Port chain #{}'.format(i))
        for plugin in path:
            if not isinstance(plugin, AreaDetector):
                if plugin.blocking_callbacks.get():
                    print(' [blocking] ', end='')

            print(' ->', plugin.name, end='')

        print()
        for plugin in path:
            if isinstance(plugin, AreaDetector):
                continue

            notes = list(check_plugin(plugin))
            if notes:
                print('* Plugin {}:'.format(plugin))
                for note, signal in notes:
                    print('\t{} = {}: {}'.format(signal.pvname,
                                                 signal.get(), note))

        # for plugin in path:
        #     print(plugin, end=' -> ')
        # print()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('ophyd_session').setLevel(logging.INFO)

    try:
        prefix = sys.argv[1]
    except IndexError:
        prefix = 'XF:03IDC-ES{Tpx:1}'

    sup_ad(prefix)
