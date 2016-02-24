from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('permissive')
class PermissiveRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    old_flag = Cpt(EpicsSignalRO, '.OFLG')
    old_status = Cpt(EpicsSignalRO, '.OVAL')
    wait_flag = Cpt(EpicsSignal, '.WFLG')

    # - display
    button_label = Cpt(EpicsSignal, '.LABL$')
