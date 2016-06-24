from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('stringin')
class StringinRecord(RecordBase):
    value = Cpt(EpicsSignal, '.VAL$', string=True)

    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    previous_value = Cpt(EpicsSignalRO, '.OVAL$', string=True)
    simulation_mode = Cpt(EpicsSignal, '.SIMM')
    simulation_value = Cpt(EpicsSignal, '.SVAL$', string=True)

    # - display
    post_archive_monitors = Cpt(EpicsSignal, '.APST')
    post_value_monitors = Cpt(EpicsSignal, '.MPST')

    # - inputs
    input_specification = Cpt(EpicsSignal, '.INP$', string=True)
    sim_input_specifctn = Cpt(EpicsSignal, '.SIOL$', string=True)
    sim_mode_location = Cpt(EpicsSignal, '.SIML$', string=True)
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')
