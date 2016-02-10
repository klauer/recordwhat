import os
import ast
import pandas as pd
from collections import namedtuple

info_path = os.path.split(os.path.abspath(__file__))[0]

_cache = {}

def _eval_field(value):
    value_map = {
        'YES': True,
        'NO': False,
        'ON': True,
        'OFF': False,
        'TRUE': True,
        'FALSE': False,
    }

    value = value.strip()
    try:
        return value_map[value]
    except KeyError:
        try:
            return ast.literal_eval(value)
        except Exception:
            return value


def load_info_file(record_type, *, data_path=None):
    cache_key = (data_path, record_type)
    if cache_key in _cache:
        return _cache[cache_key]

    if data_path is None:
        data_path = info_path

    fn = os.path.join(data_path, record_type)
    if not os.path.exists(fn):
        fn = '{}.txt'.format(fn)

    if not os.path.exists(fn):
        raise ValueError('Unknown record type {}'.format(record_type))

    df = pd.read_csv(fn, sep='\t', encoding='latin1', comment='#',
                     na_filter=False)

    ret = {}
    infotype = None
    for idx, info in df.sort_values(by=['promptgroup', 'prompt']).iterrows():
        if infotype is None:
            infotype = namedtuple('FieldInfoTuple', list(sorted(info.keys())))

        if 'DBF_NOACCESS' in info['type']:
            continue

        info = {field: _eval_field(value) for field, value in info.items()}
        ret[info['field']] = infotype(**info)

    _cache[cache_key] = ret
    return ret


link_types = ['DBF_INLINK', 'DBF_OUTLINK', 'DBF_FWDLINK']
