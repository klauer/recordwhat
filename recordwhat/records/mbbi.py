from ophyd import (EpicsSignal, EpicsSignalRO, Device)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


class MbbBit(Device):
    severity = Cpt(EpicsSignal, 'SV')
    string = Cpt(EpicsSignal, 'ST$')
    value = Cpt(EpicsSignal, 'VL')


class MbbRecordBase(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    hardware_mask = Cpt(EpicsSignalRO, '.MASK')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_monitored = Cpt(EpicsSignalRO, '.MLST')
    prev_raw_value = Cpt(EpicsSignalRO, '.ORAW')
    raw_value = Cpt(EpicsSignal, '.RVAL')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')
    states_defined = Cpt(EpicsSignalRO, '.SDEF')

    # - bits1
    bit00 = Cpt(MbbBit, '.ZR')
    bit01 = Cpt(MbbBit, '.ON')
    bit02 = Cpt(MbbBit, '.TW')
    bit03 = Cpt(MbbBit, '.TH')
    bit04 = Cpt(MbbBit, '.FR')
    bit05 = Cpt(MbbBit, '.FV')
    bit06 = Cpt(MbbBit, '.SX')
    bit07 = Cpt(MbbBit, '.SV')

    # - bits2
    bit08 = Cpt(MbbBit, '.EI')
    bit09 = Cpt(MbbBit, '.NI')
    bit10 = Cpt(MbbBit, '.TE')
    bit11 = Cpt(MbbBit, '.EL')
    bit12 = Cpt(MbbBit, '.TV')
    bit13 = Cpt(MbbBit, '.TT')
    bit14 = Cpt(MbbBit, '.FT')
    bit15 = Cpt(MbbBit, '.FF')

    # - mbb
    change_of_state_severity = Cpt(EpicsSignal, '.COSV')
    number_of_bits = Cpt(EpicsSignalRO, '.NOBT')
    shift = Cpt(EpicsSignal, '.SHFT')
    sim_mode_alarm_severity = Cpt(EpicsSignal, '.SIMS')
    unknown_state_severity = Cpt(EpicsSignal, '.UNSV')

    def __init__(self, prefix, **kwargs):
        super().__init__(prefix, **kwargs)

        self.bits  = [self.bit00, self.bit01, self.bit02, self.bit03,
                      self.bit04, self.bit05, self.bit06,
                      self.bit07,

                      self.bit08, self.bit09, self.bit10, self.bit11,
                      self.bit12, self.bit13, self.bit14, self.bit15,
                      ]


@_register_record_type('mbbi')
class MbbiRecord(MbbRecordBase):
    input_specification = Cpt(EpicsSignal, '.INP$')
    sim_input_specification = Cpt(EpicsSignal, '.SIOL$')
    simulation_value = Cpt(EpicsSignal, '.SVAL')
