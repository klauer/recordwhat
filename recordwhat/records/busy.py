from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('busy')
class BusyRecord(RecordBase):
    _rtyp = 'busy'
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_monitored = Cpt(EpicsSignalRO, '.MLST')
    prev_readback_value = Cpt(EpicsSignalRO, '.ORBV')
    raw_value = Cpt(EpicsSignal, '.RVAL')
    readback_value = Cpt(EpicsSignalRO, '.RBV')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')
    prev_raw_value = Cpt(EpicsSignalRO, '.ORAW')
    prev_value = Cpt(EpicsSignalRO, '.OVAL')

    # - alarms
    change_of_state_sevr = Cpt(EpicsSignal, '.COSV')
    one_error_severity = Cpt(EpicsSignal, '.OSV')
    zero_error_severity = Cpt(EpicsSignal, '.ZSV')

    # - display
    one_name = Cpt(EpicsSignal, '.ONAM')
    zero_name = Cpt(EpicsSignal, '.ZNAM')

    # - inputs
    sim_mode_location = Cpt(EpicsSignal, '.SIML')
    sim_output_specifctn = Cpt(EpicsSignal, '.SIOL')
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')

    # - output
    desired_output_loc = Cpt(EpicsSignal, '.DOL')
    hardware_mask = Cpt(EpicsSignalRO, '.MASK')
    invalid_outpt_action = Cpt(EpicsSignal, '.IVOA')
    invalid_output_value = Cpt(EpicsSignal, '.IVOV')
    output_mode_select = Cpt(EpicsSignal, '.OMSL')
    output_specification = Cpt(EpicsSignal, '.OUT')
    seconds_to_hold_high = Cpt(EpicsSignal, '.HIGH')
