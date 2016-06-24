from collections import OrderedDict
from ophyd import (EpicsSignal, EpicsSignalRO, Device,
                   DynamicDeviceComponent as DDC)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt,
                FormattedFieldComponent as FCpt)


class TransformInput(Device):
    previous_value = FCpt(EpicsSignalRO, '{self.prefix}.L{self.input_name}')
    value = FCpt(EpicsSignalRO, '{self.prefix}.{self.input_name}')
    link = FCpt(EpicsSignalRO, '{self.prefix}.INP{self.input_name}$',
                string=True)
    link_valid = FCpt(EpicsSignalRO, '{self.prefix}.I{self.input_name}V')
    calc_invalid = FCpt(EpicsSignal, '{self.prefix}.C{self.input_name}V')
    calculation = FCpt(EpicsSignal, '{self.prefix}.CLC{self.input_name}$',
                       string=True)
    comment = FCpt(EpicsSignal, '{self.prefix}.CMT{self.input_name}$',
                   string=True)

    def __init__(self, prefix='', *, input_name, **kwargs):
        self.input_name = input_name
        super().__init__(prefix, **kwargs)


def _make_inputs(input_names, cls=TransformInput):
    return OrderedDict(('input_{}'.format(inp.lower()),
                        (cls, '', dict(input_name=inp)))
                       for inp in input_names)


class TransformOutput(Device):
    link = FCpt(EpicsSignalRO, '{self.prefix}.OUT{self.output_name}$',
                string=True)
    link_valid = FCpt(EpicsSignalRO, '{self.prefix}.O{self.output_name}V')

    def __init__(self, prefix='', *, output_name, **kwargs):
        self.output_name = output_name
        super().__init__(prefix, **kwargs)


def _make_outputs(output_names, cls=TransformOutput):
    return OrderedDict(('output_{}'.format(outp.lower()),
                        (cls, '', dict(output_name=outp)))
                       for outp in output_names)


@_register_record_type('transform')
class TransformRecord(RecordBase):
    inputs = DDC(_make_inputs('ABCDEFGHIJKLMNOP'))
    outputs = DDC(_make_outputs('ABCDEFGHIJKLMNOP'))

    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    code_version = Cpt(EpicsSignalRO, '.VERS')

    # - common
    calc_option = Cpt(EpicsSignal, '.COPT')
    display_precision = Cpt(EpicsSignal, '.PREC')
    input_bitmap = Cpt(EpicsSignal, '.MAP')
    invalid_link_action = Cpt(EpicsSignal, '.IVLA')
    units_name = Cpt(EpicsSignal, '.EGU$', string=True)
