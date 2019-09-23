import os
# import shlex

from collections import OrderedDict

from ..util import read_file
from .db_parsimonious import (dbWalker, db_grammar,
                              template_grammar, TemplateWalker)


def ingest_db_file(fname, *, preprocessor=None):
    dw = dbWalker()
    db_text = read_file(fname)
    if preprocessor is not None:
        db_text = preprocessor(db_text)
    return dw.visit(db_grammar.parse(db_text))


def expand_macros(s, macros):
    T = TemplateWalker().visit(template_grammar.parse(s))
    macros = {k: v for k, v in macros.items() if k in T.sig.parameters}
    return T.fmt_func(**macros)


def load_records(fn, start_path, *, macros=None, ignore_nonexisting=False,
                 preprocessor=None, fallback_db_paths=None):
    '''Load records from an st.cmd file'''
    if macros is None:
        macros = {}

    # TODO dbLoadTemplate

    pv_dict = OrderedDict()
    with open(fn, 'rt') as f:
        lines = [line.strip() for line in f.readlines()]

    working_dir = start_path
    arg_strip = ''.join(("'", '"()'))
    processed_dbs = {}

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
                print('* ', line)
                print('* Path changed to', working_dir)
        elif line.startswith('dbLoadRecords'):
            records = line.partition('dbLoadRecords')[-1]
            records = records.lstrip(arg_strip)
            if records.endswith(')'):
                records = records[:-1]

            db_file, _, macro_string = records.partition(',')
            db_file = expand_macros(db_file.strip('" '), macros)

            db_macros = macros.copy()
            db_macros.update(
                **{macro.partition('=')[0].strip():
                   expand_macros(macro.partition('=')[-1].strip(), macros)
                   for macro in macro_string.strip('" ').split(',')
                   }
            )

            full_db_path = os.path.join(working_dir, db_file)
            print('DB file', full_db_path)
            if (not os.path.exists(full_db_path) and
                    fallback_db_paths is not None):
                db_file = os.path.split(full_db_path)[-1]
                potentials = [
                    os.path.join(fallback, db_file)
                    for fallback in fallback_db_paths
                    if os.path.exists(os.path.join(fallback, db_file))
                ]
                if len(potentials):
                    print('* Nonexistent', full_db_path,
                          'but alternative found', potentials[0])
                    full_db_path = potentials[0]

            if not os.path.exists(full_db_path):
                if ignore_nonexisting:
                    print('* Ignoring nonexistent database file:',
                          full_db_path)
                    continue

                raise ValueError('missing {}'.format(full_db_path))

            try:
                records = processed_dbs[full_db_path]
            except KeyError:
                records = ingest_db_file(full_db_path, preprocessor=preprocessor)
                processed_dbs[full_db_path] = records

            for rec in records:
                recname = expand_macros(rec.pvname.strip('"'), db_macros)
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

                    value = expand_macros(value, db_macros)
                    pv_dict[full_pv] = value
    return pv_dict
