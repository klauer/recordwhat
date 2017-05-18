import os
# import shlex

from collections import OrderedDict

from ..util import read_file
from .db_parsimonious import (dbWalker, db_grammar,
                              template_grammar, TemplateWalker)


def ingest_db_file(fname):
    dw = dbWalker()
    return dw.visit(db_grammar.parse(read_file(fname)))


def expand_macros(s, macros):
    T = TemplateWalker().visit(template_grammar.parse(s))
    macros = {k: v for k, v in macros.items() if k in T.sig.parameters}
    return T.fmt_func(**macros)


def load_records(fn, start_path, *, db_paths=None):
    '''Load records from an st.cmd file'''

    # TODO dbLoadTemplate

    pv_dict = OrderedDict()
    with open(fn, 'rt') as f:
        lines = [line.strip() for line in f.readlines()]

    working_dir = start_path
    arg_strip = ''.join(("'", '"()'))

    for line_no, line in enumerate(lines):
        if '#' in line:
            line = line.partition('#')[0]

        if not line:
            continue

        # print(line_no + 1, ') ', line)
        if line.startswith('chdir'):
            path = line.partition('chdir')[-1]
            path = path.strip(arg_strip)
            if path.startswith('/'):
                print('! Absolute path', line, path)
            else:
                working_dir = os.path.abspath(os.path.join(working_dir, path))
                print('* Path changed to', working_dir)
        elif line.startswith('dbLoadRecords'):
            records = line.partition('dbLoadRecords')[-1]
            records = records.strip(arg_strip)
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
            records = ingest_db_file(full_db_path)
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
