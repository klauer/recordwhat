from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('mbboDirect')
class MbbodirectRecord(RecordBase):
    _rtyp = 'mbboDirect'
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    hardware_mask = Cpt(EpicsSignalRO, '.MASK')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_monitored = Cpt(EpicsSignalRO, '.MLST')
    prev_raw_value = Cpt(EpicsSignalRO, '.ORAW')
    prev_readback_value = Cpt(EpicsSignalRO, '.ORBV')
    raw_value = Cpt(EpicsSignalRO, '.RVAL')
    readback_value = Cpt(EpicsSignalRO, '.RBV')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')

    # - bits1
    bit_0 = Cpt(EpicsSignal, '.B0')
    bit_1 = Cpt(EpicsSignal, '.B1')
    bit_2 = Cpt(EpicsSignal, '.B2')
    bit_3 = Cpt(EpicsSignal, '.B3')
    bit_4 = Cpt(EpicsSignal, '.B4')
    bit_5 = Cpt(EpicsSignal, '.B5')
    bit_6 = Cpt(EpicsSignal, '.B6')
    bit_7 = Cpt(EpicsSignal, '.B7')

    # - bits2
    bit_10 = Cpt(EpicsSignal, '.BA')
    bit_11 = Cpt(EpicsSignal, '.BB')
    bit_12 = Cpt(EpicsSignal, '.BC')
    bit_13 = Cpt(EpicsSignal, '.BD')
    bit_14 = Cpt(EpicsSignal, '.BE')
    bit_15 = Cpt(EpicsSignal, '.BF')
    bit_8 = Cpt(EpicsSignal, '.B8')
    bit_9 = Cpt(EpicsSignal, '.B9')

    # - mbb
    desired_output_loc = Cpt(EpicsSignal, '.DOL')
    invalid_outpt_action = Cpt(EpicsSignal, '.IVOA')
    invalid_output_value = Cpt(EpicsSignal, '.IVOV')
    number_of_bits = Cpt(EpicsSignalRO, '.NOBT')
    output_mode_select = Cpt(EpicsSignal, '.OMSL')
    output_specification = Cpt(EpicsSignal, '.OUT')
    shift = Cpt(EpicsSignal, '.SHFT')
    sim_mode_location = Cpt(EpicsSignal, '.SIML')
    sim_output_specifctn = Cpt(EpicsSignal, '.SIOL')
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')
