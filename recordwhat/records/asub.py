from collections import OrderedDict
from ophyd import (EpicsSignal, EpicsSignalRO, Device,
                   DynamicDeviceComponent as DDC)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt,
                FormattedFieldComponent as FCpt)


class AsubOutput(Device):
    link = FCpt(EpicsSignal, '{self.prefix}.OUT{self.output_name}$', string=True)
    type_ = FCpt(EpicsSignalRO, '{self.prefix}.FTV{self.output_name}')
    max_elements = FCpt(EpicsSignalRO, '{self.prefix}.NOV{self.output_name}')
    num_elements = FCpt(EpicsSignalRO, '{self.prefix}.NEV{self.output_name}')
    num_elements_prev = FCpt(EpicsSignalRO,
                             '{self.prefix}.ONV{self.output_name}')

    def __init__(self, prefix='', *, output_name, **kwargs):
        self.output_name = output_name
        super().__init__(prefix, **kwargs)


def _make_outputs(output_names):
    return OrderedDict(('output_{}'.format(outp.lower()),
                        (AsubOutput, '', dict(output_name=outp)))
                       for outp in output_names)


class AsubInput(Device):
    link = FCpt(EpicsSignal, '{self.prefix}.INP{self.input_name}$', string=True)
    type_ = FCpt(EpicsSignalRO, '{self.prefix}.FT{self.input_name}')
    max_elements = FCpt(EpicsSignalRO, '{self.prefix}.NO{self.input_name}')
    num_elements = FCpt(EpicsSignalRO, '{self.prefix}.NE{self.input_name}')

    def __init__(self, prefix='', *, input_name, **kwargs):
        self.input_name = input_name
        super().__init__(prefix, **kwargs)


def _make_inputs(input_names):
    return OrderedDict(('input_{}'.format(inp.lower()),
                        (AsubInput, '', dict(input_name=inp)))
                       for inp in input_names)


@_register_record_type('aSub')
class AsubRecord(RecordBase):
    inputs = DDC(_make_inputs('ABCDEFGHIJKLMNOPQRSTU'))
    outputs = DDC(_make_outputs('ABCDEFGHIJKLMNOPQRSTU'))

    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    old_return_value = Cpt(EpicsSignalRO, '.OVAL')

    # - display
    display_precision = Cpt(EpicsSignal, '.PREC')

    # - output
    output_event_flag = Cpt(EpicsSignal, '.EFLG')

    # - sub
    bad_return_severity = Cpt(EpicsSignal, '.BRSV')
    initialize_subroutine_name = Cpt(EpicsSignalRO, '.INAM$', string=True)
    old_subroutine_name = Cpt(EpicsSignalRO, '.ONAM$', string=True)
    process_subroutine_name = Cpt(EpicsSignal, '.SNAM$', string=True)
    subroutine_input_enable = Cpt(EpicsSignal, '.LFLG')
    subroutine_name_link = Cpt(EpicsSignalRO, '.SUBL$', string=True)
