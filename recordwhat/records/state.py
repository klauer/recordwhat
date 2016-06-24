from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('state')
class StateRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    prev_value = Cpt(EpicsSignalRO, '.OVAL$', string=True)
