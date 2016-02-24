from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('vs')
class VsRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    changed_control = Cpt(EpicsSignalRO, '.CHGC')
    controller_err_cnt = Cpt(EpicsSignal, '.ERR')
    controller_type = Cpt(EpicsSignal, '.TYPE')
    conv_a_log10_pressure = Cpt(EpicsSignalRO, '.LCAP')
    conv_b_log10_pressure = Cpt(EpicsSignalRO, '.LCBP')
    convectron_a_pressure = Cpt(EpicsSignalRO, '.CGAP')
    convectron_b_pressure = Cpt(EpicsSignalRO, '.CGBP')
    degas_read = Cpt(EpicsSignalRO, '.DGSR')
    fault_read = Cpt(EpicsSignalRO, '.FLTR')
    gauge_pressure = Cpt(EpicsSignalRO, '.PRES')
    ig_last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    ig_log10_pressure = Cpt(EpicsSignalRO, '.LPRS')
    ion_gauge_1_read = Cpt(EpicsSignalRO, '.IG1R')
    ion_gauge_2_read = Cpt(EpicsSignalRO, '.IG2R')
    sp_1_readback = Cpt(EpicsSignalRO, '.SP1R')
    sp_1_setpoint_set = Cpt(EpicsSignal, '.SP1S')
    sp_2_readback = Cpt(EpicsSignalRO, '.SP2R')
    sp_2_setpoint_set = Cpt(EpicsSignal, '.SP2S')
    sp_3_readback = Cpt(EpicsSignalRO, '.SP3R')
    sp_3_setpoint_set = Cpt(EpicsSignal, '.SP3S')
    sp_4_readback = Cpt(EpicsSignalRO, '.SP4R')
    sp_4_setpoint_set = Cpt(EpicsSignal, '.SP4S')
    set_point_1 = Cpt(EpicsSignalRO, '.SP1')
    set_point_2 = Cpt(EpicsSignalRO, '.SP2')
    set_point_3 = Cpt(EpicsSignalRO, '.SP3')
    set_point_4 = Cpt(EpicsSignalRO, '.SP4')
    set_point_5 = Cpt(EpicsSignalRO, '.SP5')
    set_point_6 = Cpt(EpicsSignalRO, '.SP6')
    prev_conv_a_log10_pres = Cpt(EpicsSignalRO, '.PLCA')
    prev_conv_a_pres = Cpt(EpicsSignalRO, '.PCGA')
    prev_conv_b_log10_pres = Cpt(EpicsSignalRO, '.PLCB')
    prev_conv_b_pres = Cpt(EpicsSignalRO, '.PCGB')
    prev_degas = Cpt(EpicsSignalRO, '.PDGS')
    prev_degas_pdss = Cpt(EpicsSignalRO, '.PDSS')
    prev_fault = Cpt(EpicsSignalRO, '.PFLT')
    prev_gauge_pres = Cpt(EpicsSignalRO, '.PPRE')
    prev_gauge_pres_pval = Cpt(EpicsSignalRO, '.PVAL')
    prev_ig_log10_pres = Cpt(EpicsSignalRO, '.PLPE')
    prev_ion_gauge_1 = Cpt(EpicsSignalRO, '.PI1S')
    prev_ion_gauge_1_pig1 = Cpt(EpicsSignalRO, '.PIG1')
    prev_ion_gauge_2 = Cpt(EpicsSignalRO, '.PI2S')
    prev_ion_gauge_2_pig2 = Cpt(EpicsSignalRO, '.PIG2')
    prev_sp1_readback = Cpt(EpicsSignalRO, '.PS1R')
    prev_sp1_set = Cpt(EpicsSignalRO, '.PS1S')
    prev_sp2_readback = Cpt(EpicsSignalRO, '.PS2R')
    prev_sp2_set = Cpt(EpicsSignalRO, '.PS2S')
    prev_sp3_readback = Cpt(EpicsSignalRO, '.PS3R')
    prev_sp3_set = Cpt(EpicsSignalRO, '.PS3S')
    prev_sp4_readback = Cpt(EpicsSignalRO, '.PS4R')
    prev_sp4_set = Cpt(EpicsSignalRO, '.PS4S')
    prev_set_point_1 = Cpt(EpicsSignalRO, '.PSP1')
    prev_set_point_2 = Cpt(EpicsSignalRO, '.PSP2')
    prev_set_point_3 = Cpt(EpicsSignalRO, '.PSP3')
    prev_set_point_4 = Cpt(EpicsSignalRO, '.PSP4')
    prev_set_point_5 = Cpt(EpicsSignalRO, '.PSP5')
    prev_set_point_6 = Cpt(EpicsSignalRO, '.PSP6')

    # - alarms
    ion_gauge_1_set = Cpt(EpicsSignal, '.IG1S')
    ion_gauge_2_set = Cpt(EpicsSignal, '.IG2S')

    # - bits1
    degas_set = Cpt(EpicsSignal, '.DGSS')

    # - common
    device_specification = Cpt(EpicsSignalRO, '.INP$')

    # - display
    ig_alarm_deadband = Cpt(EpicsSignal, '.HYST')
    ig_high_alarm = Cpt(EpicsSignal, '.HIGH')
    ig_high_severity = Cpt(EpicsSignal, '.HSV')
    ig_hihi_alarm = Cpt(EpicsSignal, '.HIHI')
    ig_hihi_severity = Cpt(EpicsSignal, '.HHSV')
    ig_lolo_alarm = Cpt(EpicsSignal, '.LOLO')
    ig_lolo_severity = Cpt(EpicsSignal, '.LLSV')
    ig_low_alarm = Cpt(EpicsSignal, '.LOW')
    ig_low_severity = Cpt(EpicsSignal, '.LSV')

    # - hist
    ig_pres_high_display = Cpt(EpicsSignal, '.HOPR')

    # - inputs
    ig_pres_low_display = Cpt(EpicsSignal, '.LOPR')

    # - links
    ig_log10_high_display = Cpt(EpicsSignal, '.HLPR')

    # - mbb
    ig_log10_low_display = Cpt(EpicsSignal, '.LLPR')

    # - output
    cga_pres_high_display = Cpt(EpicsSignal, '.HAPR')

    # - pid
    cga_pres_low_display = Cpt(EpicsSignal, '.LAPR')

    # - pulse
    cga_log10_high_display = Cpt(EpicsSignal, '.HALR')

    # - select
    cga_log10_low_display = Cpt(EpicsSignal, '.LALR')

    # - seq2
    cgb_pres_high_display = Cpt(EpicsSignal, '.HBPR')

    # - seq3
    cgb_pres_low_display = Cpt(EpicsSignal, '.LBPR')

    # - sub
    cgb_log10_high_display = Cpt(EpicsSignal, '.HBLR')

    # - timer
    cgb_log10_low_display = Cpt(EpicsSignal, '.LBLR')
