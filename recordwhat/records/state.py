from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('state')
class StateRecord(RecordBase):
    _rtyp = 'state'
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    prev_value = Cpt(EpicsSignalRO, '.OVAL')
