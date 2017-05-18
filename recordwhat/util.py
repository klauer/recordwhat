import subprocess
import re
import os.path

from collections import OrderedDict
from contextlib import contextmanager


default_grep_path = '/cf-update/*.dbl'


def grep_pvs(expr, *, path=None, grep_tool='/bin/grep',
             ignore_exceptions=True, switches='-he'):
    '''Grep a path of dbl listings for a specific regex

    Parameters
    ----------
    expr: str
        Grep expression
    path : str, optional
        Path to search (defaults to util.default_grep_path)
    grep_tool : str, optional
        Grep binary to use (/bin/bash)
    switches : str, optional
        Grep tool switches (-he)
    ignore_exceptions : bool, optional
        Ignore permission errors and such when the grep tool is used
    '''
    if path is None:
        path = default_grep_path

    command = ('{grep_tool} {switches} "{expr}" {path}'
               ''.format(**locals()))

    try:
        stdout = subprocess.check_output(command, stderr=subprocess.DEVNULL,
                                         shell=True)
    except subprocess.CalledProcessError as ex:
        # some permissions errors in /cf-update
        if not ignore_exceptions:
            raise
        stdout = ex.output

    stdout = stdout.decode('ascii')
    for match in stdout.split('\n'):
        match = match.strip()
        if match:
            yield match


def find_file(fn, path):
    path = ['.'] + path.split(':')
    for s_path in path:
        test_fn = os.path.join(s_path, fn)
        if os.path.exists(test_fn):
            return test_fn
    return None


def fix_includes(text, path):
    offset = 0
    while True:
        m = re.search('^(\s*include\s*"(.*)".*)$', text[offset:],
                      flags=re.MULTILINE)
        if m is None:
            break
        offset += m.start()
        full_line = m.groups()[0]
        include_file = m.groups()[1]
        fn = find_file(include_file, path)
        if fn is None:
            offset += (m.end() - m.start())
            continue
        with open(fn, 'rt') as fin:
            insert_text = fin.read()
        text = text.replace(full_line, insert_text)
    return text


def read_file(fn, path=''):
    l_dir = os.path.dirname(fn)
    if l_dir:
        path = ':'.join((l_dir, path))
    with open(fn, 'rt') as fin:
        return fix_includes(fin.read(), path)


class LocalRecordRegistry:
    def __init__(self, pv_dict=None):
        if pv_dict is None:
            pv_dict = OrderedDict()

        self.pvs = pv_dict

    @property
    def records(self):
        for pv in self.pvs:
            if '.' not in pv:
                yield pv

    def find_related_pvs(self, pvs):
        for pv, value in self.pvs.items():
            if pv in pvs:
                continue

            # print('checking', pv, value)
            value = str(value)
            if any(rec in value for rec in pvs):
                yield pv
                continue

    def find_all_related_pvs(self, pvs):
        pvs = set(pvs)
        added = True
        while added:
            added = False
            for related_pv in self.find_related_pvs(pvs):
                if related_pv not in pvs:
                    yield related_pv
                    pvs.add(related_pv)
                    added = True


class LocalPV:
    def __init__(self, pvname, **kwargs):
        self.pvname = pvname.rstrip('$')
        self.known_string = pvname.endswith('$')
        self.kwargs = kwargs
        self.connected = True
        self.auto_monitor = True
        self.timestamp = 0
        self.precision = 3

    def get(self, **kwargs):
        try:
            value = self.registry.pvs[self.pvname]
        except KeyError:
            if self.pvname.endswith('.RTYP'):
                value = 'ai'
            elif self.pvname.endswith('.FLNK'):
                value = ''
            elif self.known_string:
                value = ''
            else:
                value = 0

        print('{} = {!r}'.format(self.pvname, value))
        return value

    def put(self, value, **kwargs):
        self.registry.pvs[self.pvname] = value

    def add_callback(self, *args, **kwargs):
        pass

    wait_for_connection = add_callback


@contextmanager
def fake_epics_environment(user_registry):
    class LocalPVWithRegistry(LocalPV):
        registry = user_registry

    class LocalEpics:
        @staticmethod
        def caget(pv, **kwargs):
            return LocalPVWithRegistry(pv).get()

        @staticmethod
        def caput(pv, value, **kwargs):
            return LocalPVWithRegistry(pv).put(value)

        PV = LocalPVWithRegistry

    try:
        from . import registry
        epics = registry.epics
        registry.epics = LocalEpics

        import ophyd.signal
        ophyd.signal.PV = LocalPVWithRegistry
        ophyd.signal.epics = LocalEpics
        print('-- Set to fake epics environment')
        yield
    finally:
        print('-- Resetting to working epics environment')
        registry.epics = epics
        ophyd.signal.PV = epics.PV
        ophyd.signal.epics = epics
