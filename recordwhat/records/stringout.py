from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('stringout')
class StringoutRecord(RecordBase):
    value = Cpt(EpicsSignal, '.VAL$')

    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    previous_value = Cpt(EpicsSignalRO, '.OVAL$')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')

    # - display
    post_archive_monitors = Cpt(EpicsSignal, '.APST')
    post_value_monitors = Cpt(EpicsSignal, '.MPST')

    # - inputs
    sim_mode_location = Cpt(EpicsSignal, '.SIML$')
    sim_output_specifctn = Cpt(EpicsSignal, '.SIOL$')
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')

    # - output
    desired_output_loc = Cpt(EpicsSignal, '.DOL$')
    invalid_output_action = Cpt(EpicsSignal, '.IVOA')
    invalid_output_value = Cpt(EpicsSignal, '.IVOV$')
    output_mode_select = Cpt(EpicsSignal, '.OMSL')
    output_specification = Cpt(EpicsSignal, '.OUT$')
