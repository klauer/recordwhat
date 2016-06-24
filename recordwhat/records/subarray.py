from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('subArray')
class SubarrayRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    busy_indicator = Cpt(EpicsSignalRO, '.BUSY')
    number_elements_read = Cpt(EpicsSignalRO, '.NORD')

    # - alarms
    field_type_of_value = Cpt(EpicsSignalRO, '.FTVL')

    # - bits1
    input_specification = Cpt(EpicsSignal, '.INP$', string=True)

    # - bits2
    engineering_units_name = Cpt(EpicsSignal, '.EGU$', string=True)

    # - calc
    high_operating_range = Cpt(EpicsSignal, '.HOPR')

    # - clock
    low_operating_range = Cpt(EpicsSignal, '.LOPR')
    maximum_elements = Cpt(EpicsSignalRO, '.MALM')

    # - common
    display_precision = Cpt(EpicsSignal, '.PREC')

    # - compress
    number_of_elements = Cpt(EpicsSignal, '.NELM')

    # - convert
    substring_index = Cpt(EpicsSignal, '.INDX')
