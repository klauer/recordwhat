from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('dfanout')
class DfanoutRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    last_val_monitored = Cpt(EpicsSignalRO, '.MLST')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_archived = Cpt(EpicsSignalRO, '.ALST')
    link_selection = Cpt(EpicsSignal, '.SELN')

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

    # - display
    archive_deadband = Cpt(EpicsSignal, '.ADEL')
    display_precision = Cpt(EpicsSignal, '.PREC')
    high_operating_range = Cpt(EpicsSignal, '.HOPR')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')
    monitor_deadband = Cpt(EpicsSignal, '.MDEL')
    units_name = Cpt(EpicsSignal, '.EGU$')

    # - inputs
    desired_output_loc = Cpt(EpicsSignal, '.DOL$')

    # - links
    link_selection_loc = Cpt(EpicsSignal, '.SELL$')
    select_mechanism = Cpt(EpicsSignal, '.SELM')

    # - output
    output_mode_select = Cpt(EpicsSignal, '.OMSL')
    output_spec_a = Cpt(EpicsSignal, '.OUTA$')
    output_spec_b = Cpt(EpicsSignal, '.OUTB$')
    output_spec_c = Cpt(EpicsSignal, '.OUTC$')
    output_spec_d = Cpt(EpicsSignal, '.OUTD$')
    output_spec_e = Cpt(EpicsSignal, '.OUTE$')
    output_spec_f = Cpt(EpicsSignal, '.OUTF$')
    output_spec_g = Cpt(EpicsSignal, '.OUTG$')
    output_spec_h = Cpt(EpicsSignal, '.OUTH$')
