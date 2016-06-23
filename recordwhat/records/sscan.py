from collections import OrderedDict

from ophyd import (EpicsSignal, EpicsSignalRO)
from ophyd.device import (DynamicDeviceComponent as DDC, Device)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


class SscanDetector(Device):
    current_value = Cpt(EpicsSignalRO, 'CV')
    display_precision = Cpt(EpicsSignal, 'PR')
    engineering_units = Cpt(EpicsSignal, 'EU$')
    high_oper_range = Cpt(EpicsSignal, 'HR')
    last_value = Cpt(EpicsSignalRO, 'LV')
    low_oper_range = Cpt(EpicsSignal, 'LR')
    num_of_elements = Cpt(EpicsSignalRO, 'NE')
    pv_name = Cpt(EpicsSignal, 'PV$')
    pv_status = Cpt(EpicsSignalRO, 'NV')


def _make_detectors(low, high):
    return OrderedDict(('detector_{:02}'.format(det),
                        (SscanDetector, '.D{:02}'.format(det), {}))
                       for det in range(low, high))


class SscanPositioner(Device):
    absolute_relative = Cpt(EpicsSignal, 'AR')
    freeze_center_pos = Cpt(EpicsSignal, 'FC')
    freeze_end_pos = Cpt(EpicsSignal, 'FE')
    freeze_start_pos = Cpt(EpicsSignal, 'FS')
    freeze_step_inc = Cpt(EpicsSignal, 'FI')
    freeze_width = Cpt(EpicsSignal, 'FW')
    step_mode = Cpt(EpicsSignal, 'SM')

    current_value = Cpt(EpicsSignalRO, 'CV')
    desired_value = Cpt(EpicsSignal, 'DV')
    last_value_posted = Cpt(EpicsSignalRO, 'LV')
    previous_position = Cpt(EpicsSignalRO, 'PP')
    pv_name = Cpt(EpicsSignal, 'PV$')
    pv_status = Cpt(EpicsSignalRO, 'NV')

    center_position = Cpt(EpicsSignal, 'CP')
    end_position = Cpt(EpicsSignal, 'EP')
    scan_width = Cpt(EpicsSignal, 'WD')
    start_position = Cpt(EpicsSignal, 'SP')
    step_increment = Cpt(EpicsSignal, 'SI')

    display_precision = Cpt(EpicsSignal, 'PR')
    engineering_units = Cpt(EpicsSignal, 'EU$')
    low_operating_range = Cpt(EpicsSignal, 'LR')
    high_operating_range = Cpt(EpicsSignal, 'HR')


def _make_positioners(low, high):
    return OrderedDict(('positioner_{}'.format(pos),
                        (SscanReadback, '.P{}'.format(pos), {}))
                       for pos in range(low, high))



class SscanReadback(Device):
    readback_pv_name = Cpt(EpicsSignal, 'PV$')
    pv_status = Cpt(EpicsSignalRO, 'NV')
    rdbk_last_val_pst = Cpt(EpicsSignalRO, 'LV')
    readback_value = Cpt(EpicsSignalRO, 'CV')
    readback_delta = Cpt(EpicsSignal, 'DL')


def _make_readbacks(low, high):
    return OrderedDict(('readback_{}'.format(pos),
                        (SscanReadback, '.R{}'.format(pos), {}))
                       for pos in range(low, high))


class SscanTrigger(Device):
    command = Cpt(EpicsSignal, 'CD')
    pv_status = Cpt(EpicsSignalRO, 'NV')
    pv_name = Cpt(EpicsSignal, 'PV$')


def _make_triggers(low, high):
    return OrderedDict(('trigger_{}'.format(trig),
                        (SscanTrigger, '.T{}'.format(trig), {}))
                       for trig in range(low, high))


@_register_record_type('sscan')
class SscanRecord(RecordBase):
    detectors = DDC(_make_detectors(1, 71))
    positioners = DDC(_make_positioners(1, 5))
    readbacks = DDC(_make_readbacks(1, 5))
    triggers = DDC(_make_triggers(1, 5))

    a1_pv_status = Cpt(EpicsSignalRO, '.A1NV')
    abort_right_now = Cpt(EpicsSignalRO, '.KILL')
    after_scan_pv_status = Cpt(EpicsSignalRO, '.ASNV')
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    auto_wait_count = Cpt(EpicsSignal, '.AWCT')
    beforescan_pv_status = Cpt(EpicsSignalRO, '.BSNV')
    buffered_current_point = Cpt(EpicsSignalRO, '.BCPT')
    code_version = Cpt(EpicsSignalRO, '.VERS')
    command_field = Cpt(EpicsSignal, '.CMND')
    current_point = Cpt(EpicsSignalRO, '.CPT')
    desired_point = Cpt(EpicsSignal, '.DPT')
    execute_scan = Cpt(EpicsSignal, '.EXSC')
    go_pause_control = Cpt(EpicsSignal, '.PAUS')
    internal_execscan = Cpt(EpicsSignalRO, '.XSC')

    last_value_of_go_pause = Cpt(EpicsSignalRO, '.LPAU')
    operator_alert = Cpt(EpicsSignalRO, '.ALRT')
    point_oflast_posting = Cpt(EpicsSignalRO, '.PCPT')
    previous_xscan = Cpt(EpicsSignalRO, '.PXSC')
    record_state_msg = Cpt(EpicsSignal, '.SMSG$')
    reference_detector = Cpt(EpicsSignal, '.REFD')
    scan_data_ready = Cpt(EpicsSignalRO, '.DATA')
    scan_in_progress = Cpt(EpicsSignalRO, '.BUSY')
    scan_phase = Cpt(EpicsSignalRO, '.FAZE')
    wait_count = Cpt(EpicsSignalRO, '.WCNT')
    wait_for_client_s = Cpt(EpicsSignal, '.WAIT')
    waiting_for_client_s = Cpt(EpicsSignalRO, '.WTNG')
    waiting_for_data_storage_client = Cpt(EpicsSignal, '.AWAIT')

    # - calc
    after_scan_pv_name = Cpt(EpicsSignal, '.ASPV$')
    array_read_trigger_1_pv_name = Cpt(EpicsSignal, '.A1PV$')
    before_scan_pv_name = Cpt(EpicsSignal, '.BSPV$')

    # - common
    acquisition_mode = Cpt(EpicsSignal, '.ACQM')
    acquisition_type = Cpt(EpicsSignal, '.ACQT')
    copy_last_pt_thru = Cpt(EpicsSignal, '.COPYTO')
    data_state = Cpt(EpicsSignalRO, '.DSTATE')

    # - inputs
    a1_command = Cpt(EpicsSignal, '.A1CD')
    after_scan_command = Cpt(EpicsSignal, '.ASCD')
    array_post_time_period = Cpt(EpicsSignal, '.ATIME')
    autowait_for_data_storage_client = Cpt(EpicsSignal, '.AAWAIT')
    before_scan_command = Cpt(EpicsSignal, '.BSCD')
    detector_settling_delay = Cpt(EpicsSignal, '.DDLY')
    pause_resume_delay = Cpt(EpicsSignal, '.RDLY')
    positioner_settling_delay = Cpt(EpicsSignal, '.PDLY')
    wait_for_completion = Cpt(EpicsSignal, '.ASWAIT')
    wait_for_completion_bswait = Cpt(EpicsSignal, '.BSWAIT')

    # - links
    max_of_points = Cpt(EpicsSignalRO, '.MPTS')
    number_of_points = Cpt(EpicsSignal, '.NPTS')

    # - output
    after_scan_mode = Cpt(EpicsSignal, '.PASM')
    freeze_flag_override = Cpt(EpicsSignal, '.FFO')
    freeze_num_of_points = Cpt(EpicsSignal, '.FPTS')
