from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('ai')
class AiRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    current_raw_value = Cpt(EpicsSignal, '.RVAL')
    initialized = Cpt(EpicsSignalRO, '.INIT')
    last_val_monitored = Cpt(EpicsSignalRO, '.MLST')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_archived = Cpt(EpicsSignalRO, '.ALST')
    lastbreak_point = Cpt(EpicsSignalRO, '.LBRK')
    previous_raw_value = Cpt(EpicsSignalRO, '.ORAW')
    raw_offset_obsolete = Cpt(EpicsSignal, '.ROFF')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')
    simulation_value = Cpt(EpicsSignal, '.SVAL')

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

    # - convert
    adjustment_offset = Cpt(EpicsSignal, '.AOFF')
    adjustment_slope = Cpt(EpicsSignal, '.ASLO')
    engineer_units_full = Cpt(EpicsSignal, '.EGUF')
    engineer_units_low = Cpt(EpicsSignal, '.EGUL')
    linearization = Cpt(EpicsSignal, '.LINR')
    raw_to_egu_offset = Cpt(EpicsSignal, '.EOFF')
    raw_to_egu_slope = Cpt(EpicsSignal, '.ESLO')
    smoothing = Cpt(EpicsSignal, '.SMOO')

    # - display
    archive_deadband = Cpt(EpicsSignal, '.ADEL')
    display_precision = Cpt(EpicsSignal, '.PREC')
    engineering_units = Cpt(EpicsSignal, '.EGU')
    high_operating_range = Cpt(EpicsSignal, '.HOPR')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')
    monitor_deadband = Cpt(EpicsSignal, '.MDEL')

    # - inputs
    input_specification = Cpt(EpicsSignal, '.INP')
    sim_input_specifctn = Cpt(EpicsSignal, '.SIOL')
    sim_mode_location = Cpt(EpicsSignal, '.SIML')
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')
