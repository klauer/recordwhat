from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('ao')
class AoRecord(RecordBase):
    _rtyp = 'ao'
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    current_raw_value = Cpt(EpicsSignal, '.RVAL')
    initialized = Cpt(EpicsSignalRO, '.INIT')
    last_val_monitored = Cpt(EpicsSignalRO, '.MLST')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_archived = Cpt(EpicsSignalRO, '.ALST')
    lastbreak_point = Cpt(EpicsSignalRO, '.LBRK')
    output_value = Cpt(EpicsSignal, '.OVAL')
    prev_readback_value = Cpt(EpicsSignalRO, '.ORBV')
    previous_raw_value = Cpt(EpicsSignalRO, '.ORAW')
    previous_value = Cpt(EpicsSignalRO, '.PVAL')
    raw_offset_obsolete = Cpt(EpicsSignal, '.ROFF')
    readback_value = Cpt(EpicsSignalRO, '.RBV')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')
    was_oval_modified = Cpt(EpicsSignalRO, '.OMOD')

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
    egu_to_raw_offset = Cpt(EpicsSignal, '.EOFF')
    egu_to_raw_slope = Cpt(EpicsSignal, '.ESLO')
    eng_units_full = Cpt(EpicsSignal, '.EGUF')
    eng_units_low = Cpt(EpicsSignal, '.EGUL')
    linearization = Cpt(EpicsSignal, '.LINR')

    # - display
    archive_deadband = Cpt(EpicsSignal, '.ADEL')
    display_precision = Cpt(EpicsSignal, '.PREC')
    engineering_units = Cpt(EpicsSignal, '.EGU')
    high_operating_range = Cpt(EpicsSignal, '.HOPR')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')
    monitor_deadband = Cpt(EpicsSignal, '.MDEL')

    # - inputs
    sim_mode_location = Cpt(EpicsSignal, '.SIML')
    sim_output_specifctn = Cpt(EpicsSignal, '.SIOL')
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')

    # - output
    desired_output_loc = Cpt(EpicsSignal, '.DOL')
    drive_high_limit = Cpt(EpicsSignal, '.DRVH')
    drive_low_limit = Cpt(EpicsSignal, '.DRVL')
    invalid_output_action = Cpt(EpicsSignal, '.IVOA')
    invalid_output_value = Cpt(EpicsSignal, '.IVOV')
    out_full_incremental = Cpt(EpicsSignal, '.OIF')
    output_mode_select = Cpt(EpicsSignal, '.OMSL')
    output_rate_of_chang = Cpt(EpicsSignal, '.OROC')
    output_specification = Cpt(EpicsSignal, '.OUT')
