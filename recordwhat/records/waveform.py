from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('waveform')
class WaveformRecord(RecordBase):
    _rtyp = 'waveform'
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    busy_indicator = Cpt(EpicsSignalRO, '.BUSY')
    hash_of_onchange_data = Cpt(EpicsSignal, '.HASH')
    number_elements_read = Cpt(EpicsSignalRO, '.NORD')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')

    # - display
    display_precision = Cpt(EpicsSignal, '.PREC')
    engineering_units_name = Cpt(EpicsSignal, '.EGU')
    high_operating_range = Cpt(EpicsSignal, '.HOPR')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')
    post_archive_monitors = Cpt(EpicsSignal, '.APST')
    post_value_monitors = Cpt(EpicsSignal, '.MPST')

    # - inputs
    input_specification = Cpt(EpicsSignal, '.INP')
    sim_input_specifctn = Cpt(EpicsSignal, '.SIOL')
    sim_mode_location = Cpt(EpicsSignal, '.SIML')
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')

    # - wave
    field_type_of_value = Cpt(EpicsSignalRO, '.FTVL')
    number_of_elements = Cpt(EpicsSignalRO, '.NELM')
    rearm_the_waveform = Cpt(EpicsSignal, '.RARM')
