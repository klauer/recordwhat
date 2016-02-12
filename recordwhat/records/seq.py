from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('seq')
class SeqRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    constant_input_1 = Cpt(EpicsSignal, '.DO1')
    constant_input_10 = Cpt(EpicsSignal, '.DOA')
    constant_input_2 = Cpt(EpicsSignal, '.DO2')
    constant_input_3 = Cpt(EpicsSignal, '.DO3')
    constant_input_4 = Cpt(EpicsSignal, '.DO4')
    constant_input_5 = Cpt(EpicsSignal, '.DO5')
    constant_input_6 = Cpt(EpicsSignal, '.DO6')
    constant_input_7 = Cpt(EpicsSignal, '.DO7')
    constant_input_8 = Cpt(EpicsSignal, '.DO8')
    constant_input_9 = Cpt(EpicsSignal, '.DO9')
    link_selection = Cpt(EpicsSignal, '.SELN')

    # - display
    display_precision = Cpt(EpicsSignal, '.PREC')

    # - inputs
    link_selection_loc = Cpt(EpicsSignal, '.SELL')
    select_mechanism = Cpt(EpicsSignal, '.SELM')

    # - seq1
    delay_1 = Cpt(EpicsSignal, '.DLY1')
    delay_2 = Cpt(EpicsSignal, '.DLY2')
    delay_3 = Cpt(EpicsSignal, '.DLY3')
    input_link_2 = Cpt(EpicsSignal, '.DOL2')
    input_link_3 = Cpt(EpicsSignal, '.DOL3')
    input_link1 = Cpt(EpicsSignal, '.DOL1')
    output_link_1 = Cpt(EpicsSignal, '.LNK1')
    output_link_2 = Cpt(EpicsSignal, '.LNK2')
    output_link_3 = Cpt(EpicsSignal, '.LNK3')

    # - seq2
    delay_4 = Cpt(EpicsSignal, '.DLY4')
    delay_5 = Cpt(EpicsSignal, '.DLY5')
    delay_6 = Cpt(EpicsSignal, '.DLY6')
    input_link_4 = Cpt(EpicsSignal, '.DOL4')
    input_link_5 = Cpt(EpicsSignal, '.DOL5')
    input_link_6 = Cpt(EpicsSignal, '.DOL6')
    output_link_4 = Cpt(EpicsSignal, '.LNK4')
    output_link_5 = Cpt(EpicsSignal, '.LNK5')
    output_link_6 = Cpt(EpicsSignal, '.LNK6')

    # - seq3
    delay_10 = Cpt(EpicsSignal, '.DLYA')
    delay_7 = Cpt(EpicsSignal, '.DLY7')
    delay_8 = Cpt(EpicsSignal, '.DLY8')
    delay_9 = Cpt(EpicsSignal, '.DLY9')
    input_link_10 = Cpt(EpicsSignal, '.DOLA')
    input_link_7 = Cpt(EpicsSignal, '.DOL7')
    input_link_8 = Cpt(EpicsSignal, '.DOL8')
    input_link_9 = Cpt(EpicsSignal, '.DOL9')
    output_link_10 = Cpt(EpicsSignal, '.LNKA')
    output_link_7 = Cpt(EpicsSignal, '.LNK7')
    output_link_8 = Cpt(EpicsSignal, '.LNK8')
    output_link_9 = Cpt(EpicsSignal, '.LNK9')
