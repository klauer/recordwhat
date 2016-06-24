from collections import OrderedDict
from ophyd import (EpicsSignal, EpicsSignalRO, Device,
                   DynamicDeviceComponent as DDC)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt,
                FormattedFieldComponent as FCpt)


class CalcInput(Device):
    previous_value = FCpt(EpicsSignalRO, '{self.prefix}.L{self.input_name}')
    value = FCpt(EpicsSignalRO, '{self.prefix}.{self.input_name}')
    link = FCpt(EpicsSignalRO, '{self.prefix}.INP{self.input_name}$', string=True)

    def __init__(self, prefix='', *, input_name, **kwargs):
        self.input_name = input_name
        super().__init__(prefix, **kwargs)


def _make_inputs(input_names, cls=CalcInput):
    return OrderedDict(('input_{}'.format(inp.lower()),
                        (cls, '', dict(input_name=inp)))
                       for inp in input_names)


@_register_record_type('calc')
class CalcRecord(RecordBase):
    inputs = DDC(_make_inputs('ABCDEFGHIJKL'))

    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    last_val_monitored = Cpt(EpicsSignalRO, '.MLST')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_archived = Cpt(EpicsSignalRO, '.ALST')

    # - alarms
    alarm_deadband = Cpt(EpicsSignal, '.HYST')
    high_alarm_limit = Cpt(EpicsSignal, '.HIGH')
    high_severity = Cpt(EpicsSignal, '.HSV')
    hihi_alarm_limit = Cpt(EpicsSignal, '.HIHI')
    hihi_severity = Cpt(EpicsSignal, '.HHSV')
    lolo_alarm_limit = Cpt(EpicsSignal, '.LOLO')
    lolo_severity = Cpt(EpicsSignal, '.LLSV')
    low_alarm_limit = Cpt(EpicsSignal, '.LOW')
    low_severity = Cpt(EpicsSignal, '.LSV')

    # - calc
    calculation = Cpt(EpicsSignal, '.CALC$', string=True)

    # - display
    archive_deadband = Cpt(EpicsSignal, '.ADEL')
    display_precision = Cpt(EpicsSignal, '.PREC')
    high_operating_rng = Cpt(EpicsSignal, '.HOPR')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')
    monitor_deadband = Cpt(EpicsSignal, '.MDEL')
    units_name = Cpt(EpicsSignal, '.EGU$', string=True)
