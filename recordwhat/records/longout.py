from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('longout')
class LongoutRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    last_val_monitored = Cpt(EpicsSignalRO, '.MLST')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_archived = Cpt(EpicsSignalRO, '.ALST')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')

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
    units_name = Cpt(EpicsSignal, '.EGU$', string=True)

    # - inputs
    sim_mode_location = Cpt(EpicsSignal, '.SIML$', string=True)
    sim_output_specifctn = Cpt(EpicsSignal, '.SIOL$', string=True)
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')

    # - output
    desired_output_loc = Cpt(EpicsSignal, '.DOL$', string=True)
    drive_high_limit = Cpt(EpicsSignal, '.DRVH')
    drive_low_limit = Cpt(EpicsSignal, '.DRVL')
    invalid_output_action = Cpt(EpicsSignal, '.IVOA')
    invalid_output_value = Cpt(EpicsSignal, '.IVOV')
    output_mode_select = Cpt(EpicsSignal, '.OMSL')
    output_specification = Cpt(EpicsSignal, '.OUT$', string=True)
