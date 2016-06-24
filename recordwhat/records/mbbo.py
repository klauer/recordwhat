from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (_register_record_type,
                FieldComponent as Cpt)

from .mbbi import MbbRecordBase


@_register_record_type('mbbo')
class MbboRecord(MbbRecordBase):
    prev_readback_value = Cpt(EpicsSignalRO, '.ORBV')
    raw_value = Cpt(EpicsSignal, '.RVAL')
    readback_value = Cpt(EpicsSignalRO, '.RBV')

    simulation_mode = Cpt(EpicsSignal, '.SIMM')
    states_defined = Cpt(EpicsSignalRO, '.SDEF')

    # - mbb
    desired_output_loc = Cpt(EpicsSignal, '.DOL$')
    invalid_outpt_action = Cpt(EpicsSignal, '.IVOA')
    invalid_output_value = Cpt(EpicsSignal, '.IVOV')

    output_mode_select = Cpt(EpicsSignal, '.OMSL')
    output_specification = Cpt(EpicsSignal, '.OUT$')
    sim_output_specifctn = Cpt(EpicsSignal, '.SIOL$')
