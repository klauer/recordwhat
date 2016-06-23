import pytest
import epics

import recordwhat
from .util import skip_if_pv_unavailable


motor_pv = 'XF:31IDA-OP{Tbl-Ax:X1}Mtr'

records = [
    ('ai', 'Py:ai1'),
    ('ao', 'Py:ao1'),
    ('bi', 'Py:bi1'),
    ('bo', 'Py:bo1'),
    ('fanout', 'Py:mylinker'),
    ('longin', 'Py:long1'),
    ('longout', 'Py:long2'),
    ('mbbo', 'Py:mbbo1'),
    ('stringin', 'Py:str1'),
    ('stringout', 'Py:str2'),
    ('subArray', 'Py:ZeroLenSubArr1'),
    ('waveform', 'Py:char128')
]


@pytest.fixture(scope='module')
def motor_rec():
    skip_if_pv_unavailable(motor_pv)
    return recordwhat.get_record_by_name(motor_pv, read_attrs=[])


def smoke_test_motor(motor_rec):
    rec = motor_rec
    # get a specific field's value
    print('steps_per_revolution =', rec.steps_per_revolution.get())

    # or access to the signal itself
    print('steps_per_revolution signal =', rec.steps_per_revolution)
    print()

    # or ask for *all* the values
    print(rec.get())

    # poke around with field metadata
    metadata = dict(rec.field_metadata())
    print('description field type', metadata['description'].type)
    print('derivative gain metadata', metadata['derivative_gain'])

    print('description metadata', rec.description.metadata)

    print('in links', list(rec.attrs_of_type('DBF_INLINK')))
    print('all links', list(rec.attrs_of_type(['DBF_INLINK', 'DBF_OUTLINK',
                                               'DBF_FWDLINK'])))

@pytest.mark.parametrize('rtyp, record', records)
def test_records(rtyp, record):
    skip_if_pv_unavailable(record)
    rec = recordwhat.get_record_by_name(record, read_attrs=[])

    assert recordwhat.get_record_class(rtyp) is rec.__class__

    metadata = dict(rec.field_metadata())
    print('metadata', metadata)

    print('description metadata', rec.description.metadata)

    print('in links', list(rec.attrs_of_type('DBF_INLINK')))
    print('all links', list(rec.attrs_of_type(['DBF_INLINK', 'DBF_OUTLINK',
                                               'DBF_FWDLINK'])))
