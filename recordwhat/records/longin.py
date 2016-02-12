from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('longin')
class LonginRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    last_val_monitored = Cpt(EpicsSignalRO, '.MLST')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_archived = Cpt(EpicsSignalRO, '.ALST')
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

    # - display
    archive_deadband = Cpt(EpicsSignal, '.ADEL')
    high_operating_range = Cpt(EpicsSignal, '.HOPR')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')
    monitor_deadband = Cpt(EpicsSignal, '.MDEL')
    units_name = Cpt(EpicsSignal, '.EGU')

    # - inputs
    input_specification = Cpt(EpicsSignal, '.INP')
    sim_input_specifctn = Cpt(EpicsSignal, '.SIOL')
    sim_mode_location = Cpt(EpicsSignal, '.SIML')
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')
