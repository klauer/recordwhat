from collections import OrderedDict
from ophyd import (EpicsSignal, EpicsSignalRO, Device,
                   DynamicDeviceComponent as DDC)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt,
                FormattedFieldComponent as FCpt)


class AcalcoutArrayInput(Device):
    pv_status = FCpt(EpicsSignalRO, '{self.prefix}.I{self.input_name}')
    pv_name = FCpt(EpicsSignal, '{self.prefix}.IN{self.input_name}$')

    def __init__(self, prefix='', *, input_name, **kwargs):
        self.input_name = input_name
        super().__init__(prefix, **kwargs)


class AcalcoutInput(Device):
    pv_status = FCpt(EpicsSignalRO, '{self.prefix}.IN{self.input_name}V')
    previous_value = FCpt(EpicsSignalRO, '{self.prefix}.P{self.input_name}')
    value = FCpt(EpicsSignalRO, '{self.prefix}.{self.input_name}')
    pv_name = FCpt(EpicsSignal, '{self.prefix}.INP{self.input_name}$')

    def __init__(self, prefix='', *, input_name, **kwargs):
        self.input_name = input_name
        super().__init__(prefix, **kwargs)


def _make_inputs(input_names, cls):
    return OrderedDict(('input_{}'.format(inp.lower()),
                        (cls, '', dict(input_name=inp)))
                       for inp in input_names)


@_register_record_type('acalcout')
class AcalcoutRecord(RecordBase):
    array_inputs = DDC(_make_inputs(['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG',
                                     'HH', 'II', 'JJ', 'KK', 'LL'],
                                    AcalcoutArrayInput)
                       )
    inputs = DDC(_make_inputs('ABCDEFGHIJKL', AcalcoutInput))


    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    array_mod = Cpt(EpicsSignalRO, '.AMASK')
    array_size_reported_to_clients = Cpt(EpicsSignal, '.SIZE')
    calc_valid = Cpt(EpicsSignal, '.CLCV')
    calc_active = Cpt(EpicsSignalRO, '.CACT')
    calc_status = Cpt(EpicsSignalRO, '.CSTAT')
    code_version = Cpt(EpicsSignalRO, '.VERS')

    last_val_monitored = Cpt(EpicsSignalRO, '.MLST')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_archived = Cpt(EpicsSignalRO, '.ALST')
    ocal_valid = Cpt(EpicsSignal, '.OCLV')
    out_pv_status = Cpt(EpicsSignalRO, '.OUTV')
    output_delay_active = Cpt(EpicsSignalRO, '.DLYA')
    output_value = Cpt(EpicsSignal, '.OVAL')

    prev_value_of_oval = Cpt(EpicsSignal, '.POVL')
    previous_value = Cpt(EpicsSignal, '.PVAL')
    wait_for_completion = Cpt(EpicsSignal, '.WAIT')
    new_array_value_mask = Cpt(EpicsSignalRO, '.NEWM')

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
    output_execute_delay = Cpt(EpicsSignal, '.ODLY')

    # - calc
    calculation = Cpt(EpicsSignal, '.CALC$')
    output_calculation = Cpt(EpicsSignal, '.OCAL$')
    output_data_opt = Cpt(EpicsSignal, '.DOPT')
    output_execute_opt = Cpt(EpicsSignal, '.OOPT')

    # - clock
    event_to_issue = Cpt(EpicsSignal, '.OEVT')

    # - display
    archive_deadband = Cpt(EpicsSignal, '.ADEL')
    display_precision = Cpt(EpicsSignal, '.PREC')
    high_operating_rng = Cpt(EpicsSignal, '.HOPR')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')
    monitor_deadband = Cpt(EpicsSignal, '.MDEL')
    units_name = Cpt(EpicsSignal, '.EGU$')

    # - output
    invalid_output_action = Cpt(EpicsSignal, '.IVOA')
    invalid_output_value = Cpt(EpicsSignal, '.IVOV')
    output_link = Cpt(EpicsSignal, '.OUT$')

    # - wave
    elem_s_in_use = Cpt(EpicsSignal, '.NUSE')
    number_of_elements = Cpt(EpicsSignalRO, '.NELM')
