from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('epid')
class EpidRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    controlled_value = Cpt(EpicsSignalRO, '.CVAL')
    d_component = Cpt(EpicsSignalRO, '.D')
    delta_t = Cpt(EpicsSignal, '.DT')
    error = Cpt(EpicsSignalRO, '.ERR')
    i_component = Cpt(EpicsSignal, '.I')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_archived = Cpt(EpicsSignalRO, '.ALST')
    last_value_monitored = Cpt(EpicsSignalRO, '.MLST')
    output_value = Cpt(EpicsSignalRO, '.OVAL')
    p_component = Cpt(EpicsSignalRO, '.P')
    prev_output = Cpt(EpicsSignalRO, '.OVLP')
    prev_controlled_value = Cpt(EpicsSignalRO, '.CVLP')
    prev_d_component = Cpt(EpicsSignalRO, '.DP')
    prev_delta_t = Cpt(EpicsSignal, '.DTP')
    prev_error = Cpt(EpicsSignalRO, '.ERRP')
    prev_i_component = Cpt(EpicsSignal, '.IP')
    prev_p_component = Cpt(EpicsSignalRO, '.PP')

    # - alarms
    alarm_deadband = Cpt(EpicsSignal, '.HYST')
    high_deviation_limit = Cpt(EpicsSignal, '.HIGH')
    high_severity = Cpt(EpicsSignal, '.HSV')
    hihi_deviation_limit = Cpt(EpicsSignal, '.HIHI')
    hihi_severity = Cpt(EpicsSignal, '.HHSV')
    lolo_deviation_limit = Cpt(EpicsSignal, '.LOLO')
    lolo_severity = Cpt(EpicsSignal, '.LLSV')
    low_deviation_limit = Cpt(EpicsSignal, '.LOW')
    low_severity = Cpt(EpicsSignal, '.LSV')

    # - display
    archive_deadband = Cpt(EpicsSignal, '.ADEL')
    display_precision = Cpt(EpicsSignal, '.PREC')
    engineering_units = Cpt(EpicsSignal, '.EGU$')
    high_drive_limit = Cpt(EpicsSignal, '.DRVH')
    high_operating_range = Cpt(EpicsSignal, '.HOPR')
    low_drive_limit = Cpt(EpicsSignal, '.DRVL')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')
    monitor_deadband = Cpt(EpicsSignal, '.MDEL')

    # - inputs
    controlled_value_loc = Cpt(EpicsSignal, '.INP$')

    # - pid
    derivative_gain = Cpt(EpicsSignal, '.KD')
    feedback_mode = Cpt(EpicsSignal, '.FMOD')
    feedback_on_off = Cpt(EpicsSignal, '.FBON')
    intergral_gain = Cpt(EpicsSignal, '.KI')
    min_delta_t = Cpt(EpicsSignal, '.MDT')
    output_deadband = Cpt(EpicsSignal, '.ODEL')
    output_location = Cpt(EpicsSignal, '.OUTL$')
    prev_feedback_on_off = Cpt(EpicsSignal, '.FBOP')
    proportional_gain = Cpt(EpicsSignal, '.KP')
    readback_trigger = Cpt(EpicsSignal, '.TRIG$')
    setpoint_location = Cpt(EpicsSignal, '.STPL$')
    setpoint_mode_select = Cpt(EpicsSignal, '.SMSL')
    trigger_value = Cpt(EpicsSignal, '.TVAL')
