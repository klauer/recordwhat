import sys
import logging
import subprocess
from ophyd import AreaDetector
from ophyd.areadetector.plugins import (PluginBase, get_areadetector_plugin,
                                        ProcessPlugin)
from .util import grep_pvs


logger = logging.getLogger(__name__)


def get_plugins_by_prefix(det_prefix, *, path=None, **kwargs):
    '''Grep a list of pvs for a detector prefix; get all plugin instances'''
    # Grep the pv list directory for things with the areadetector prefix
    pvs = grep_pvs('^{}.*EnableCallbacks$'.format(det_prefix),
                   path=path, **kwargs)

    # Strip off EnableCallbacks
    pvs = [pv.split('EnableCallbacks')[0]
           for pv in pvs]
    return get_plugins_by_prefix_list(pvs)


def get_plugins_by_prefix_list(prefixes):
    '''Grep a list of pvs for a detector prefix; get all plugin instances'''
    for prefix in prefixes:
        try:
            # Try to get the plugin type
            plugin = get_areadetector_plugin(prefix)
        except ValueError as ex:
            # Or give up
            logger.debug('Get plugin failed', exc_info=ex)
        else:
            plugin.wait_for_connection()
            yield plugin


def check_plugin(plugin):
    '''Plugin information that might be noteworthy'''

    # TODO unnused, probably can be removed
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


def get_port_dictionary(plugins):
    '''Given a list of plugin, get all ports mapped to plugins'''
    return {plugin.port_name.get(): plugin
            for plugin in plugins}


def graph_ports_by_prefix(prefix):
    '''Convenience function, given prefix return a port graph

    This first greps the default database list directory, gets the port
    mapping dictionary, then generates the graph.

    Parameters
    ----------
    prefix : str
        The detector prefix

    Returns
    -------
    graph : graphviz.Digraph
    '''
    from .graph import port_graph

    plugins = get_plugins_by_prefix(prefix)
    ad_ports = get_port_dictionary(plugins)
    return port_graph(ad_ports)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('ophyd_session').setLevel(logging.INFO)

    try:
        prefix = sys.argv[1]
    except IndexError:
        prefix = 'XF:03IDC-ES{Tpx:1}'

    try:
        save_to = sys.argv[2]
    except IndexError:
        save_to = 'ad_ports'

    graph = graph_ports_by_prefix(prefix)
    print('Saved to', graph.render(save_to))
