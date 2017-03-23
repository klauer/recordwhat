from ophyd import (EpicsSignal, EpicsSignalRO,
                   DynamicDeviceComponent as DDC)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)

from ophyd.scaler import _scaler_fields


NUM_CH = 64


def _string_scaler_fields(*args, **kwargs):
    '''Use _scaler_fields, but append $ to suffixes to allow long strings'''
    info = _scaler_fields(*args, **kwargs)
    for attr, (cls, prefix, kw) in list(info.items()):
        info[attr] = (cls, prefix + '$', kw)
    return info


@_register_record_type('scaler')
class ScalerRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    code_version = Cpt(EpicsSignalRO, '.VERS')
    count = Cpt(EpicsSignal, '.CNT')

    number_of_channels = Cpt(EpicsSignalRO, '.NCH')
    oneshot_autocount = Cpt(EpicsSignal, '.CONT')
    prev_count = Cpt(EpicsSignalRO, '.PCNT')
    scaler_state = Cpt(EpicsSignalRO, '.SS')
    timer = Cpt(EpicsSignalRO, '.T')
    user_state = Cpt(EpicsSignalRO, '.US')

    # - common
    auto_display_rate_hz = Cpt(EpicsSignal, '.RAT1')
    auto_mode_delay = Cpt(EpicsSignal, '.DLY1')
    cnt_output = Cpt(EpicsSignal, '.COUT$', string=True)
    cnt_output_prompt = Cpt(EpicsSignal, '.COUTP$', string=True)

    channels = DDC(_scaler_fields(EpicsSignalRO, 'chan', '.S',
                                  range(1, NUM_CH + 1)))
    presets = DDC(_scaler_fields(EpicsSignal, 'preset', '.PR',
                                 range(1, NUM_CH + 1)))
    gates = DDC(_scaler_fields(EpicsSignal, 'gate', '.G',
                               range(1, NUM_CH + 1)))
    count_directions = DDC(_scaler_fields(EpicsSignal, 'direction', '.D',
                                          range(1, NUM_CH + 1)))
    names = DDC(_string_scaler_fields(EpicsSignal, 'name', '.NM',
                                      range(1, NUM_CH + 1)))

    delay = Cpt(EpicsSignal, '.DLY')
    display_precision = Cpt(EpicsSignal, '.PREC')
    display_rate_hz = Cpt(EpicsSignal, '.RATE')

    output_specification = Cpt(EpicsSignalRO, '.OUT$', string=True)

    time_preset = Cpt(EpicsSignal, '.TP')
    time_preset_tp1 = Cpt(EpicsSignal, '.TP1')
    time_base_freq = Cpt(EpicsSignal, '.FREQ')
    units_name = Cpt(EpicsSignal, '.EGU$', string=True)
