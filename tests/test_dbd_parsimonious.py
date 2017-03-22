from recordwhat.parsers.dbd_parsimonious import (
    dbd_grammar, dbdField, dbdRecordType, RecordWalker,
    stream_dbd)
from collections import OrderedDict


def test_round_trip():
    fields = OrderedDict()
    for pg in ('AA', 'BB'):
        for j in range(5):
            nm = '{}{}'.format(pg, j)
            fields[nm] = dbdField(
                nm,
                'DBF_CHAR',
                prompt='"test p {}"'.format(j))

    rec = dbdRecordType(name='test',
                        fields=fields)
    test_str = '\n'.join(stream_dbd(rec))
    p = dbd_grammar.parse(test_str)
    rec2 = RecordWalker().visit(p)['test']

    assert rec == rec2
