from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('compress')
class CompressRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    compress_value_buffer = Cpt(EpicsSignalRO, '.CVB')
    compressed_array_inx = Cpt(EpicsSignalRO, '.INX')
    number_used = Cpt(EpicsSignalRO, '.NUSE')
    number_of_elements_in_working_buffer = Cpt(EpicsSignalRO, '.INPN')
    offset = Cpt(EpicsSignalRO, '.OFF')
    old_number_used = Cpt(EpicsSignalRO, '.OUSE')
    reset = Cpt(EpicsSignal, '.RES')

    # - alarms
    compression_algorithm = Cpt(EpicsSignal, '.ALG')

    # - compress
    init_high_interest_lim = Cpt(EpicsSignal, '.IHIL')
    init_low_interest_lim = Cpt(EpicsSignal, '.ILIL')
    input_specification = Cpt(EpicsSignal, '.INP$')
    n_to_1_compression = Cpt(EpicsSignal, '.N')
    number_of_values = Cpt(EpicsSignalRO, '.NSAM')

    # - display
    display_precision = Cpt(EpicsSignal, '.PREC')
    engineeringunits = Cpt(EpicsSignal, '.EGU$')
    high_operating_range = Cpt(EpicsSignal, '.HOPR')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')
