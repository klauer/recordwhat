from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('aao')
class AaoRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    hash_of_onchange_data = Cpt(EpicsSignal, '.HASH')
    number_elements_read = Cpt(EpicsSignalRO, '.NORD')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')

    # - alarms
    display_precision = Cpt(EpicsSignal, '.PREC')

    # - bits1
    output_specification = Cpt(EpicsSignal, '.OUT$')

    # - bits2
    engineering_units_name = Cpt(EpicsSignal, '.EGU$')

    # - calc
    high_operating_range = Cpt(EpicsSignal, '.HOPR')

    # - clock
    low_operating_range = Cpt(EpicsSignal, '.LOPR')

    # - compress
    number_of_elements = Cpt(EpicsSignalRO, '.NELM')

    # - convert
    field_type_of_value = Cpt(EpicsSignalRO, '.FTVL')

    # - display
    post_archive_monitors = Cpt(EpicsSignal, '.APST')
    post_value_monitors = Cpt(EpicsSignal, '.MPST')

    # - hist
    sim_mode_location = Cpt(EpicsSignal, '.SIML$')

    # - inputs
    sim_output_specifctn = Cpt(EpicsSignal, '.SIOL$')
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')
