import os
import re
import logging
import glob
import textwrap

from functools import partial


from .. import record_info
from .. import records

logger = logging.getLogger(__name__)
record_info_path = os.path.split(os.path.abspath(record_info.__file__))[0]
record_source_path = os.path.split(os.path.abspath(records.__file__))[0]

base_header = '''\
from ophyd import (Device, EpicsSignal, EpicsSignalRO,
                   Component as Cpt)

'''

record_header = '''\
from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)

'''


def load_dbd_derived(fn):
    '''Load field information (tsv derived from the database definitions)'''
    import pandas as pd

    df = pd.read_csv(fn, sep='\t', encoding='latin1', comment='#',
                     na_filter=False)

    group = None
    for idx, info in df.sort_values(by=['promptgroup', 'prompt']).iterrows():
        field = info['field']
        if 'DBF_NOACCESS' in info['type']:
            continue

        prompt = info['prompt']
        short_desc = prompt
        attr_name = short_desc.lower()
        attr_name = re.sub('[^A-Za-z_0-9]', '_', attr_name)
        attr_name = re.sub('_+', '_', attr_name)
        attr_name = re.sub('^_', '', attr_name)
        attr_name = re.sub('_$', '', attr_name)

        group = info['promptgroup'].replace('GUI_', '')
        group = group.lower()

        if 'SPC_NOMOD' in info['special']:
            cls = 'EpicsSignalRO'
        else:
            cls = 'EpicsSignal'

        yield dict(cls=cls,
                   field=field,
                   short_desc=short_desc,
                   attr_name=attr_name,
                   doc=prompt,
                   group=group,
                   type=info['type'],
                   )


def load_wiki_derived(fn):
    '''Load field information (tsv derived from the database definitions)'''
    import pandas as pd

    df = pd.read_csv(fn, sep='\t', encoding='latin1', index_col='Field',
                     comment='#', na_filter=False)
    for field, info in sorted(df.iterrows()):
        short_desc = info['Description']
        attr_name = short_desc.lower().replace(' ', '_')
        doc = info['Notes'].strip('"')
        doc = doc.replace("'", '"')
        yield dict(cls='EpicsSignal',
                   field=field,
                   short_desc=short_desc,
                   attr_name=attr_name,
                   doc=doc,
                   group='',
                   type=None,
                   )

    if 'VAL' not in df:
        yield dict(cls='EpicsSignal',
                   field='VAL',
                   short_desc='value',
                   attr_name='value',
                   doc='Record value',
                   group='',
                   type=None,
                   )


def generate(cls, info_gen, *, super_='Device', skip_attrs=None,
             skip_fields={}, test_record=None, include_docs=False,
             include_header=True, record_type=None):

    if skip_attrs is None:
        skip_attrs = {}

    if skip_fields is None:
        skip_fields = {}

    if include_header:
        if record_type is not None:
            yield "@_register_record_type('{}')".format(record_type)
        yield 'class {cls}({super}):'.format(cls=cls, super=super_)

    group = None

    attrs = {}
    for info in info_gen:
        attr = info['attr_name']
        if info['attr_name'] in skip_attrs:
            continue
        if info['field'] in skip_fields:
            continue

        if attr == '':
            attr = info['field'].lower()

        if attr in attrs:
            # TODO sometime the short desc isn't enough for a unique attr name
            #      so tag on the field name if necessary
            if not attr:
                info['attr_name'] = info['field'].lower()
            else:
                info['attr_name'] = '_'.join((attr, info['field'].lower()))
            attr = info['attr_name']

        info['attr_name'] = attr
        attrs[attr] = info

        if info['group'] and info['group'] != group:
            yield ''
            yield '    # - {}'.format(info['group'])
            group = info['group']

        type_ = info['type']
        if type_ == 'DBF_STRING' or type_ in record_info.link_types:
            # EPICS originally supported 40 chars for strings, but extended it
            # at some point, still keeping backward compatibility. So to
            # request long strings, you have to add a $ at the end of the PV
            # name...
            if not info['field'].endswith('$'):
                info['field'] += '$'

        if test_record is not None:
            import epics
            pv_name = '.'.join((test_record, info['field']))
            pv = epics.PV(pv_name)
            if not pv.wait_for_connection(timeout=0.3):
                logger.error('Failed to connect to %s; skipping %s', pv_name,
                             attr)
                continue
            if pv.access in ('read/write', ):
                pass
            elif pv.access in ('read-only', ):
                info['cls'] += 'RO'
                logger.info('Setting %s to be read-only from test signal',
                            attr)
            # pv.disconnect()

        if include_docs:
            code = ("    {attr_name} = Cpt({cls}, '.{field}', doc='{doc}')"
                    "".format(**info))
            indent = ' ' * (code.index('(') + 1) + "'"
            wrapper = textwrap.TextWrapper(initial_indent='',
                                           subsequent_indent=indent, width=78)
            code_lines = wrapper.wrap(code)
            code_lines[:-1] = [line.rstrip() + " '"
                               for line in code_lines[:-1]]
            yield from code_lines
        else:
            yield "    {attr_name} = Cpt({cls}, '.{field}')".format(**info)


def generate_all(info_path=record_info_path, dest_path=record_source_path):
    logging.basicConfig(level=logging.DEBUG)
    getfn = partial(os.path.join, info_path)

    os.makedirs(dest_path, exist_ok=True)

    source_fn = os.path.join(dest_path, 'record.py')
    print('-- all.txt -> {} --'.format(source_fn))
    with open(source_fn, 'wt', encoding='utf-8') as f:
        print(base_header, file=f)
        skip_fields = ('DSET PPN PPNR DPVT RDES RSET ASP LSET MLIS SPVT MLOK '
                       'BKPT TIME'.split(' '))
        for line in generate('RecordBase',
                             load_wiki_derived(getfn('all.txt')),
                             skip_fields=skip_fields,
                             test_record='XF:31IDA-OP{Tbl-Ax:X1}Mtr'):
            print(line, file=f)

    base_fields = [info['field'] for info in
                   load_wiki_derived(getfn('all.txt'))]

    txt_to_record = {fn: os.path.split(fn)[1][:-4]
                     for fn in glob.glob(getfn('*.txt'))}
    for fn, rtyp in txt_to_record.items():
        if rtyp in ('all', ):
            continue

        python_fn = (rtyp + '.py').lower()
        source_fn = os.path.join(dest_path, python_fn)
        print('-- {} -> {} --'.format(fn, source_fn))
        with open(source_fn, 'wt', encoding='utf-8') as f:
            print(record_header, file=f)
            rec = rtyp.capitalize() + 'Record'
            for line in generate(rec, load_dbd_derived(fn),
                                 super_='RecordBase', skip_fields=base_fields,
                                 record_type=rtyp):
                print(line, file=f)


if __name__ == '__main__':
    if input('Re-generate all records? [yn]') in ('Y', 'y'):
        generate_all()
