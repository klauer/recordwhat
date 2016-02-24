from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('timestamp')
class TimestampRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    current_raw_value = Cpt(EpicsSignal, '.RVAL')
    previous_value = Cpt(EpicsSignalRO, '.OVAL$')

    # - inputs
    time_stamp_type = Cpt(EpicsSignal, '.TST')
