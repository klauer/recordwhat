from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('aao')
class AaoRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    hash_of_onchange_data = Cpt(EpicsSignal, '.HASH')
    number_elements_read = Cpt(EpicsSignalRO, '.NORD')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')

    # - alarms
    display_precision = Cpt(EpicsSignal, '.PREC')

    # - bits1
    output_specification = Cpt(EpicsSignal, '.OUT$', string=True)

    # - bits2
    engineering_units_name = Cpt(EpicsSignal, '.EGU$', string=True)

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
    sim_mode_location = Cpt(EpicsSignal, '.SIML$', string=True)

    # - inputs
    sim_output_specifctn = Cpt(EpicsSignal, '.SIOL$', string=True)
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')
