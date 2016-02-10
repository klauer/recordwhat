from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('digitel')
class DigitelRecord(RecordBase):
    _rtyp = 'digitel'
    acc_current = Cpt(EpicsSignalRO, '.ACCI')
    acc_power = Cpt(EpicsSignalRO, '.ACCW')
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    bake_installed = Cpt(EpicsSignalRO, '.BKIN')
    bake_readback = Cpt(EpicsSignalRO, '.BAKR')
    bake_time_mode_read = Cpt(EpicsSignalRO, '.S3BR')
    bake_time_read = Cpt(EpicsSignalRO, '.S3TR')
    bake_time_set = Cpt(EpicsSignal, '.S3TS')
    cooldown_mode = Cpt(EpicsSignalRO, '.CMOR')
    cooldown_time = Cpt(EpicsSignalRO, '.COOL')
    current = Cpt(EpicsSignalRO, '.CRNT')
    cycle_count = Cpt(EpicsSignalRO, '.CYCL')
    error_count = Cpt(EpicsSignalRO, '.ERR')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    mod_flags = Cpt(EpicsSignalRO, '.FLGS')
    mode_readback = Cpt(EpicsSignalRO, '.MODR')
    pressure_log10_form = Cpt(EpicsSignalRO, '.LVAL')
    pump_type = Cpt(EpicsSignalRO, '.PTYP')
    sp1_hvi_readback = Cpt(EpicsSignalRO, '.S1VR')
    sp1_hy_readback = Cpt(EpicsSignalRO, '.S1HR')
    sp1_hysteresis = Cpt(EpicsSignal, '.S1HS')
    sp1_mode_readback = Cpt(EpicsSignalRO, '.S1MR')
    sp1_sp_readback = Cpt(EpicsSignalRO, '.SP1R')
    sp1_setpoint = Cpt(EpicsSignal, '.SP1S')
    sp2_hvi_readback = Cpt(EpicsSignalRO, '.S2VR')
    sp2_hy_readback = Cpt(EpicsSignalRO, '.S2HR')
    sp2_hysteresis = Cpt(EpicsSignal, '.S2HS')
    sp2_mode_readback = Cpt(EpicsSignalRO, '.S2MR')
    sp2_sp_readback = Cpt(EpicsSignalRO, '.SP2R')
    sp2_setpoint = Cpt(EpicsSignal, '.SP2S')
    sp3_hvi_readback = Cpt(EpicsSignalRO, '.S3VR')
    sp3_hy_readback = Cpt(EpicsSignalRO, '.S3HR')
    sp3_hysteresis = Cpt(EpicsSignal, '.S3HS')
    sp3_mode_readback = Cpt(EpicsSignalRO, '.S3MR')
    sp3_sp_readback = Cpt(EpicsSignalRO, '.SP3R')
    sp3_setpoint = Cpt(EpicsSignal, '.SP3S')
    setpoint_1 = Cpt(EpicsSignalRO, '.SET1')
    setpoint_2 = Cpt(EpicsSignalRO, '.SET2')
    setpoint_3 = Cpt(EpicsSignalRO, '.SET3')
    setpoint_flags = Cpt(EpicsSignalRO, '.SPFG')
    sim_mode_value = Cpt(EpicsSignal, '.SIMM')
    sim_value_current = Cpt(EpicsSignal, '.SVCR')
    sim_value_mode = Cpt(EpicsSignal, '.SVMO')
    sim_value_sp1 = Cpt(EpicsSignal, '.SVS1')
    sim_value_sp2 = Cpt(EpicsSignal, '.SVS2')
    time_online = Cpt(EpicsSignalRO, '.TONL')
    voltage = Cpt(EpicsSignalRO, '.VOLT')
    init_acc_current = Cpt(EpicsSignalRO, '.IACI')
    init_acc_power = Cpt(EpicsSignalRO, '.IACW')
    init_bake_installed = Cpt(EpicsSignalRO, '.IBKN')
    init_error_count = Cpt(EpicsSignalRO, '.IERR')
    init_bake = Cpt(EpicsSignalRO, '.IBAK')
    init_cooldown_time = Cpt(EpicsSignalRO, '.ICOL')
    init_current = Cpt(EpicsSignalRO, '.ICRN')
    init_mode = Cpt(EpicsSignalRO, '.IMOD')
    init_pressure = Cpt(EpicsSignalRO, '.IVAL')
    init_pressure_log10 = Cpt(EpicsSignalRO, '.ILVA')
    init_pump_type = Cpt(EpicsSignalRO, '.IPTY')
    init_set1 = Cpt(EpicsSignalRO, '.ISP1')
    init_set2 = Cpt(EpicsSignalRO, '.ISP2')
    init_set3 = Cpt(EpicsSignalRO, '.ISP3')
    init_sp1 = Cpt(EpicsSignalRO, '.IS1')
    init_sp1_hvi = Cpt(EpicsSignalRO, '.II1')
    init_sp1_hy = Cpt(EpicsSignalRO, '.IH1')
    init_sp1_mode = Cpt(EpicsSignalRO, '.IM1')
    init_sp2 = Cpt(EpicsSignalRO, '.IS2')
    init_sp2_hvi = Cpt(EpicsSignalRO, '.II2')
    init_sp2_hy = Cpt(EpicsSignalRO, '.IH2')
    init_sp2_mode = Cpt(EpicsSignalRO, '.IM2')
    init_sp3 = Cpt(EpicsSignalRO, '.IS3')
    init_sp3_hvi = Cpt(EpicsSignalRO, '.II3')
    init_sp3_hy = Cpt(EpicsSignalRO, '.IH3')
    init_sp3_bake_time = Cpt(EpicsSignalRO, '.IT3')
    init_sp3_bake_time_md = Cpt(EpicsSignalRO, '.IB3')
    init_sp3_mode = Cpt(EpicsSignalRO, '.IM3')
    init_tonl = Cpt(EpicsSignalRO, '.ITON')
    init_voltage = Cpt(EpicsSignalRO, '.IVOL')

    # - alarms
    alarm_deadband = Cpt(EpicsSignal, '.HYST')
    display_mode = Cpt(EpicsSignal, '.DSPL')
    pressure_high_alarm = Cpt(EpicsSignal, '.HIGH')
    pressure_high_severity = Cpt(EpicsSignal, '.HSV')
    pressure_hihi_alarm = Cpt(EpicsSignal, '.HIHI')
    pressure_hihi_severity = Cpt(EpicsSignal, '.HHSV')
    pressure_lolo_alarm = Cpt(EpicsSignal, '.LOLO')
    pressure_lolo_severity = Cpt(EpicsSignal, '.LLSV')
    pressure_low_alarm = Cpt(EpicsSignal, '.LOW')
    pressure_low_severity = Cpt(EpicsSignal, '.LSV')

    # - bits1
    keyboard_lock = Cpt(EpicsSignal, '.KLCK')

    # - bits2
    bake = Cpt(EpicsSignal, '.BAKS')
    controller_type = Cpt(EpicsSignal, '.TYPE')
    mode = Cpt(EpicsSignal, '.MODS')

    # - common
    device_specification = Cpt(EpicsSignalRO, '.INP')

    # - display
    log_pres_display_hi = Cpt(EpicsSignal, '.HLPR')
    log_pres_display_lo = Cpt(EpicsSignal, '.LLPR')
    sim_location_current = Cpt(EpicsSignalRO, '.SLCR')
    sim_location_mode = Cpt(EpicsSignalRO, '.SLMO')
    sim_location_sp1 = Cpt(EpicsSignalRO, '.SLS1')
    sim_location_sp2 = Cpt(EpicsSignalRO, '.SLS2')
    sim_mode_location = Cpt(EpicsSignalRO, '.SIML')

    # - hist
    sp1_mode = Cpt(EpicsSignal, '.S1MS')

    # - inputs
    sp1_hv_interlock = Cpt(EpicsSignal, '.S1VS')

    # - links
    sp2_mode = Cpt(EpicsSignal, '.S2MS')
    sp3_mode = Cpt(EpicsSignal, '.S3MS')

    # - mbb
    sp2_hv_interlock = Cpt(EpicsSignal, '.S2VS')
    sp3_hv_interlock = Cpt(EpicsSignal, '.S3VS')

    # - motor
    bake_time_mode_set = Cpt(EpicsSignal, '.S3BS')

    # - scan
    voltage_display_lo = Cpt(EpicsSignal, '.LVTR')

    # - seq2
    pressure_display_hi = Cpt(EpicsSignal, '.HOPR')

    # - seq3
    pressure_display_lo = Cpt(EpicsSignal, '.LOPR')

    # - sub
    current_display_hi = Cpt(EpicsSignal, '.HCTR')

    # - timer
    current_display_lo = Cpt(EpicsSignal, '.LCTR')

    # - wave
    voltage_display_hi = Cpt(EpicsSignal, '.HVTR')
