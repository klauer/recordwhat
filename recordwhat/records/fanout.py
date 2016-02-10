from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('fanout')
class FanoutRecord(RecordBase):
    _rtyp = 'fanout'
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    link_selection = Cpt(EpicsSignal, '.SELN')

    # - links
    forward_link_1 = Cpt(EpicsSignal, '.LNK1')
    forward_link_2 = Cpt(EpicsSignal, '.LNK2')
    forward_link_3 = Cpt(EpicsSignal, '.LNK3')
    forward_link_4 = Cpt(EpicsSignal, '.LNK4')
    forward_link_5 = Cpt(EpicsSignal, '.LNK5')
    forward_link_6 = Cpt(EpicsSignal, '.LNK6')
    link_selection_loc = Cpt(EpicsSignal, '.SELL')
    select_mechanism = Cpt(EpicsSignal, '.SELM')
