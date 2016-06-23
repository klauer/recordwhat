from collections import OrderedDict

from ophyd import (EpicsSignal, EpicsSignalRO)
from ophyd.device import (DynamicDeviceComponent as DDC, Device)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


class McaRegion(Device):
    counts = Cpt(EpicsSignalRO, '')
    net_counts = Cpt(EpicsSignalRO, 'N')
    preset = Cpt(EpicsSignal, 'P')
    bkgrnd_chans = Cpt(EpicsSignal, 'BG')
    high_channel = Cpt(EpicsSignal, 'HI')
    is_preset = Cpt(EpicsSignal, 'IP')
    low_channel = Cpt(EpicsSignal, 'LO')
    name_of_region = Cpt(EpicsSignal, 'NM$')


def _make_regions(low, high):
    return OrderedDict(('region_{:02}'.format(region),
                        (McaRegion, '.R{}'.format(region), {}))
                       for region in range(low, high))


@_register_record_type('mca')
class McaRecord(RecordBase):
    acquiring = Cpt(EpicsSignalRO, '.ACQG')
    actual_counts_in_pregio = Cpt(EpicsSignalRO, '.ACT')
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    average_dead_time = Cpt(EpicsSignalRO, '.DTIM')
    code_version = Cpt(EpicsSignalRO, '.VERS')
    elapsed_live_time = Cpt(EpicsSignal, '.ELTM')
    elapsed_real_time = Cpt(EpicsSignal, '.ERTM')
    instantaneous_dead_time = Cpt(EpicsSignalRO, '.IDTIM')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_read_time = Cpt(EpicsSignalRO, '.RTIM')
    message_not_acknowledge = Cpt(EpicsSignalRO, '.NACK')
    monitor_map = Cpt(EpicsSignalRO, '.MMAP')
    new_roi_value_map = Cpt(EpicsSignalRO, '.NEWR')
    new_value_map = Cpt(EpicsSignalRO, '.NEWV')
    number_of_channels_read = Cpt(EpicsSignalRO, '.NORD')
    roi_monitor_map = Cpt(EpicsSignalRO, '.RMAP')
    reading_array = Cpt(EpicsSignalRO, '.RDNG')
    reading_status = Cpt(EpicsSignalRO, '.RDNS')
    regions = DDC(_make_regions(0, 32))
    simulation_mode = Cpt(EpicsSignal, '.SIMM')

    # - alarms
    alarm_deadband = Cpt(EpicsSignal, '.HYST')
    high_deviation_limit = Cpt(EpicsSignal, '.HIGH')
    high_severity = Cpt(EpicsSignal, '.HSV')
    hihi_deviation_limit = Cpt(EpicsSignal, '.HIHI')
    hihi_severity = Cpt(EpicsSignal, '.HHSV')
    lolo_deviation_limit = Cpt(EpicsSignal, '.LOLO')
    lolo_severity = Cpt(EpicsSignal, '.LLSV')
    low_deviation_limit = Cpt(EpicsSignal, '.LOW')
    low_severity = Cpt(EpicsSignal, '.LSV')

    # - common
    number_of_channels_to_use = Cpt(EpicsSignal, '.NUSE')
    calibration_offset = Cpt(EpicsSignal, '.CALO')
    calibration_quadratic = Cpt(EpicsSignal, '.CALQ')
    calibration_slope = Cpt(EpicsSignal, '.CALS')
    channel_advance_prescale = Cpt(EpicsSignal, '.PSCL')
    channel_advance_source = Cpt(EpicsSignal, '.CHAS')
    dwell_time_per_channel = Cpt(EpicsSignal, '.DWEL')
    erase_start_acquire = Cpt(EpicsSignal, '.ERST')
    erase_array = Cpt(EpicsSignal, '.ERAS')
    field_type_of_value = Cpt(EpicsSignalRO, '.FTVL')
    max_number_of_channels = Cpt(EpicsSignalRO, '.NMAX')
    mode_pha_mcs_list = Cpt(EpicsSignal, '.MODE')
    preset_count_high_channel = Cpt(EpicsSignal, '.PCTH')
    preset_count_low_channel = Cpt(EpicsSignal, '.PCTL')
    preset_counts = Cpt(EpicsSignal, '.PCT')
    preset_live_time = Cpt(EpicsSignal, '.PLTM')
    preset_number_of_sweeps = Cpt(EpicsSignal, '.PSWP')
    preset_real_time = Cpt(EpicsSignal, '.PRTM')
    read_array = Cpt(EpicsSignal, '.READ')

    start_acquire = Cpt(EpicsSignal, '.STRT')
    stop_acquire = Cpt(EpicsSignal, '.STOP')
    time_sequence = Cpt(EpicsSignal, '.SEQ')
    two_theta = Cpt(EpicsSignal, '.TTH')

    # - display
    acquisition_stop_time = Cpt(EpicsSignalRO, '.STIM$')
    calibration_units_name = Cpt(EpicsSignal, '.EGU$')
    display_precision = Cpt(EpicsSignal, '.PREC')
    high_operating_range = Cpt(EpicsSignal, '.HOPR')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')

    # - inputs
    input_specification = Cpt(EpicsSignalRO, '.INP$')
    sim_input_specifctn = Cpt(EpicsSignalRO, '.SIOL$')
    sim_mode_location = Cpt(EpicsSignalRO, '.SIML$')
    sim_mode_alarm_severity = Cpt(EpicsSignal, '.SIMS')
