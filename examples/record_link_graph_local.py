import os
# import shlex
import sys

from collections import OrderedDict

import ophyd
import ophyd.signal

from recordwhat.util import read_file
from recordwhat.graph import graph_links_with_subgraphs
from recordwhat import registry
from recordwhat.parsers.db_parsimonious import (dbWalker, db_grammar)


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


class LocalPV:
    def __init__(self, pvname, **kwargs):
        self.pvname = pvname.rstrip('$')
        self.known_string = pvname.endswith('$')
        self.kwargs = kwargs

        try:
            int(self.pvname)
            float(self.pvname)
        except ValueError:
            self.connected = False
        else:
            self.connected = True

        self.connected = True

    def get(self, **kwargs):
        try:
            value = self.registry.pvs[self.pvname]
        except KeyError:

            if self.pvname.endswith('.RTYP'):
                value = 'ai'
            elif self.known_string:
                value = ''
            else:
                value = 0

        # print('get(', self.pvname, ') = ', value)
        return value

    def add_callback(self, *args, **kwargs):
        pass

    wait_for_connection = add_callback


class LocalEpics:
    @staticmethod
    def caget(pv, **kwargs):
        return LocalPV(pv).get()

    PV = LocalPV


registry.epics = LocalEpics
ophyd.signal.PV = LocalPV
ophyd.signal.epics = LocalEpics


def injest_db_file(fname):
    dw = dbWalker()
    return dw.visit(db_grammar.parse(read_file(fname)))


def expand_macros(s, macros):
    for mname, mvalue in macros.items():
        s = s.replace('$({})'.format(mname), mvalue)
        s = s.replace('$({},undefined)'.format(mname), mvalue)

    return s


def load_st_cmd(
        fn='/Users/klauer/iocs/hgvpu-current/iocBoot/ioc-und1-uc01/st.cmd',
        start_path='/Users/klauer/iocs/hgvpu-current/iocBoot/ioc-und1-uc01/',
        db_paths=None):
    pv_dict = OrderedDict()
    with open(fn, 'rt') as f:
        lines = [line.strip() for line in f.readlines()]

    working_dir = start_path

    for line_no, line in enumerate(lines):
        if '#' in line:
            line = line.partition('#')[0]

        if not line:
            continue

        # print(line_no + 1, ') ', line)
        if line.startswith('chdir'):
            path = line.partition('chdir')[-1]
            path = path.strip('()"')
            if path.startswith('/'):
                print('! Absolute path', line, path)
            else:
                working_dir = os.path.abspath(os.path.join(working_dir, path))
                print('* Path changed to', working_dir)
        elif line.startswith('dbLoadRecords'):
            records = line.partition('dbLoadRecords')[-1]
            records = records.strip('()"')
            db_file, _, macros = records.partition(',')
            db_file = db_file.strip('" ')
            macros = macros.strip('" ')
            macros = {macro.partition('=')[0].strip():
                      macro.partition('=')[-1].strip()
                      for macro in macros.split(',')
                      }

            full_db_path = os.path.join(working_dir, db_file)
            print('DB file', full_db_path, macros)
            if not os.path.exists(full_db_path):
                raise ValueError('missing {}'.format(full_db_path))
            records = injest_db_file(full_db_path)
            for rec in records:
                recname = expand_macros(rec.pvname.strip('"'), macros)
                rec.fields['RTYP'] = rec.rtype
                if 'VAL' not in rec.fields:
                    rec.fields['VAL'] = ''

                if 'VAL' in rec.fields:
                    rec.fields[''] = rec.fields['VAL']
                if 'FLNK' not in rec.fields:
                    rec.fields['FLNK'] = ''

                for field, fieldstruct in rec.fields.items():
                    if field:
                        full_pv = '{}.{}'.format(recname, field)
                    else:
                        full_pv = recname

                    if hasattr(fieldstruct, 'value'):
                        value = fieldstruct.value.strip('" ')
                    else:
                        value = fieldstruct.strip('" ')

                    value = expand_macros(value, macros)
                    pv_dict[full_pv] = value
    return pv_dict


def main(records, *, graph_fn='graph',
         st_cmd='/Users/klauer/iocs/hgvpu-current/iocBoot/ioc-und1-uc01/st.cmd',
         start_path='/Users/klauer/iocs/hgvpu-current/iocBoot/ioc-und1-uc01/'):
    import logging
    logging.getLogger('recordwhat.graph').setLevel(logging.DEBUG)
    logging.basicConfig()

    reg = LocalRecordRegistry(load_st_cmd(fn=st_cmd, start_path=start_path))
    LocalPV.registry = reg

    print('total loaded', len(reg.pvs), 'records', len(list(reg.records)))
    print()
    print()

    # if len(sys.argv) == 1:
    #     records = tuple(rec for rec in reg.records if not (':SR_' in rec))
    # else:

    records = list(records)
    added = True
    while added:
        added = False
        for pv, value in reg.pvs.items():
            if pv in records:
                continue

            if any(rec in str(value) for rec in records):
                print('adding', pv)
                added = True
                records.append(pv)
                continue

    import graphviz
    graph = graphviz.Digraph(format='pdf')
    graph = graph_links_with_subgraphs(*records)
    print('rendered graph to', graph.render(graph_fn))
    return graph


if __name__ == '__main__':
    records = list(sys.argv[1:])
    main(records)
