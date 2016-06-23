import pytest

from recordwhat.graph import graph_links_with_subgraphs
from recordwhat.graph import graph_links

from .util import skip_if_pv_unavailable


single_records = [
    'XF:31IDA-OP{Tbl-Ax:FakeMtr}-SP_',
    'Py:xbi',
    'Py:mylinker',
]


record_groups = [('XF:31IDA-OP{Tbl-Ax:FakeMtr}-SP',
                  'XF:31IDA-OP{Tbl-Ax:FakeMtr}-SP_',
                  'XF:31IDA-OP{Tbl-Ax:X1}Mtr',),
                 ('Py:mylinker', 'Py:wave_test'),
                 ]


@pytest.mark.parametrize('record', single_records)
def test_graph_link_single_record(record):
    skip_if_pv_unavailable(record)
    graph_links(record)


@pytest.mark.parametrize('records', record_groups)
def test_graph_link_records(records):
    skip_if_pv_unavailable(records[0])
    graph_links_with_subgraphs(*records)
