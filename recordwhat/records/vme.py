from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('vme')
class VmeRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    status_array = Cpt(EpicsSignal, '.SARR')

    # - common
    read_write = Cpt(EpicsSignal, '.RDWT')
    vme_address_mode = Cpt(EpicsSignal, '.AMOD')
    vme_data_size = Cpt(EpicsSignal, '.DSIZ')

    # - display
    address_increment_1_4 = Cpt(EpicsSignal, '.AINC')
    max_number_of_values = Cpt(EpicsSignal, '.NMAX')
    number_of_values_to_r_w = Cpt(EpicsSignal, '.NUSE')
    vme_address_hex = Cpt(EpicsSignal, '.ADDR')
