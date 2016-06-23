from collections import OrderedDict

from ophyd import (EpicsSignal, EpicsSignalRO,
                   Device, DynamicDeviceComponent as DDC)
from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt,
                FormattedFieldComponent as FCpt)


class SwaitInput(Device):
    pv_status = FCpt(EpicsSignalRO, '{self.prefix}.IN{self.input_name}V')
    last_value = FCpt(EpicsSignal, '{self.prefix}.L{self.input_name}')
    value = FCpt(EpicsSignal, '{self.prefix}.{self.input_name}')
    pv_name = FCpt(EpicsSignal, '{self.prefix}.IN{self.input_name}N$')
    causes_io_intr = FCpt(EpicsSignal, '{self.prefix}.IN{self.input_name}P')

    def __init__(self, prefix='', *, input_name, **kwargs):
        self.input_name = input_name
        super().__init__(prefix, **kwargs)


def _make_inputs(input_names):
    return OrderedDict(('input_{}'.format(inp.lower()),
                        (SwaitInput, '', dict(input_name=inp)))
                       for inp in input_names)


@_register_record_type('swait')
class SwaitRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    calc_valid = Cpt(EpicsSignal, '.CLCV')
    code_version = Cpt(EpicsSignalRO, '.VERS')
    dol_pv_status = Cpt(EpicsSignalRO, '.DOLV')

    inputs = DDC(_make_inputs(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                               'J', 'K', 'L']))
    initialized = Cpt(EpicsSignalRO, '.INIT')
    last_val_monitored = Cpt(EpicsSignalRO, '.MLST')
    last_value_archived = Cpt(EpicsSignalRO, '.ALST')
    out_pv_status = Cpt(EpicsSignalRO, '.OUTV')
    old_value = Cpt(EpicsSignal, '.OVAL')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')
    simulation_value = Cpt(EpicsSignal, '.SVAL')

    # - alarms
    high_operating_range = Cpt(EpicsSignal, '.HOPR')
    output_execute_delay = Cpt(EpicsSignal, '.ODLY')

    # - bits1
    low_operating_range = Cpt(EpicsSignal, '.LOPR')

    # - calc
    dol_pv_name = Cpt(EpicsSignal, '.DOLN$')
    out_pv_name = Cpt(EpicsSignal, '.OUTN$')
    output_data_option = Cpt(EpicsSignal, '.DOPT')
    output_execute_opt = Cpt(EpicsSignal, '.OOPT')

    # - clock
    archive_deadband = Cpt(EpicsSignal, '.ADEL')
    calculation = Cpt(EpicsSignal, '.CALC$')
    desired_output_data = Cpt(EpicsSignal, '.DOLD')
    event_to_issue = Cpt(EpicsSignal, '.OEVT')
    monitor_deadband = Cpt(EpicsSignal, '.MDEL')

    # - common
    display_precision = Cpt(EpicsSignal, '.PREC')

    # - pulse
    sim_input_specifctn = Cpt(EpicsSignal, '.SIOL$')
    sim_mode_location = Cpt(EpicsSignal, '.SIML$')

    # - select
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')
