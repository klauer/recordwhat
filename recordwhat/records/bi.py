from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('bi')
class BiRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    hardware_mask = Cpt(EpicsSignalRO, '.MASK')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_monitored = Cpt(EpicsSignalRO, '.MLST')
    raw_value = Cpt(EpicsSignal, '.RVAL')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')
    simulation_value = Cpt(EpicsSignal, '.SVAL')
    prev_raw_value = Cpt(EpicsSignalRO, '.ORAW')

    # - alarms
    zero_error_severity = Cpt(EpicsSignal, '.ZSV')

    # - bits1
    one_error_severity = Cpt(EpicsSignal, '.OSV')

    # - bits2
    change_of_state_svr = Cpt(EpicsSignal, '.COSV')

    # - calc
    zero_name = Cpt(EpicsSignal, '.ZNAM')

    # - clock
    one_name = Cpt(EpicsSignal, '.ONAM')

    # - inputs
    input_specification = Cpt(EpicsSignal, '.INP')
    sim_input_specifctn = Cpt(EpicsSignal, '.SIOL')
    sim_mode_location = Cpt(EpicsSignal, '.SIML')
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')
