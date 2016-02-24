from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('histogram')
class HistogramRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    collection_control = Cpt(EpicsSignal, '.CMD')
    collection_status = Cpt(EpicsSignalRO, '.CSTA')
    counts_since_monitor = Cpt(EpicsSignalRO, '.MCNT')
    element_width = Cpt(EpicsSignalRO, '.WDTH')
    signal_value = Cpt(EpicsSignal, '.SGNL')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')
    simulation_value = Cpt(EpicsSignal, '.SVAL')

    # - display
    display_precision = Cpt(EpicsSignal, '.PREC')
    high_operating_range = Cpt(EpicsSignal, '.HOPR')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')

    # - hist
    lower_signal_limit = Cpt(EpicsSignal, '.LLIM')
    monitor_count_deadband = Cpt(EpicsSignal, '.MDEL')
    monitor_seconds_dband = Cpt(EpicsSignal, '.SDEL')
    num_of_array_elements = Cpt(EpicsSignalRO, '.NELM')
    upper_signal_limit = Cpt(EpicsSignal, '.ULIM')

    # - inputs
    signal_value_location = Cpt(EpicsSignal, '.SVL$')
    sim_input_specifctn = Cpt(EpicsSignal, '.SIOL$')
    sim_mode_location = Cpt(EpicsSignal, '.SIML$')
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')
