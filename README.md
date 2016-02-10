recordwhat
==========

Example
=======

```python
import recordwhat

rec = recordwhat.get_record_by_name('XF:31IDA-OP{Tbl-Ax:X1}Mtr', read_attrs=[])

# get a specific field's value
print('steps_per_revolution =', rec.steps_per_revolution.get())

# or access to the signal itself
print('steps_per_revolution signal =', rec.steps_per_revolution)
print()

# or ask for *all* the values
print(rec.get())
```

Output:
```python
steps_per_revolution = 200
steps_per_revolution signal = EpicsSignal(read_pv='XF:31IDA-OP{Tbl-Ax:X1}Mtr.SREV', name='XF:31IDA-OP{Tbl-Ax:X1}Mtr_steps_per_revolution', parent='XF:31IDA-OP{Tbl-Ax:X1}Mtr', value=200, timestamp=1455045145.501072, pv_kw={}, auto_monitor=False, string=False, write_pv='XF:31IDA-OP{Tbl-Ax:X1}Mtr.SREV', limits=False, put_complete=False)

MotorRecordTuple(alarm_acknowledge_severity=0, alarm_acknowledge_transient=1,
                 access_security_group='', description='Delta',
                 scan_disable_input_link_value=0, disable_putfields=0,
                 disable_alarm_severity=0, disable_value=1, device_type=0,
                 event_number=0, forward_link='0', lock_count=0,
                 record_name='XF:31IDA-OP{Tbl-Ax:X1}Mtr', new_alarm_severity=0,
                 new_alarm_status=0, processing_active=0, scan_phase_number=0,
                 process_at_initialization=0, priority=0, process_record=0,
                 dbputfield_process=0, reprocess=0, scanning_rate=0,
                 scan_disable_input_link='', current_alarm_severity=0,
                 trace_processing=0, time_stamp_event=0,
                 time_stamp_event_link='', val_undefined=0, value=1.0,
                 alarm_status=0, at_home=0, card_number=0,
                 code_version=6.809999942779541, dial_desired_value_egu=1.0,
                 dial_readback_value=1.0, difference_dval_drbv=0.0,
                 difference_rval_rrbv=0, direction_of_travel=0,
                 freeze_offset=0, home_forward=0, home_reverse=0,
                 jog_motor_forward=0, jog_motor_reverse=0,
                 last_dial_des_val_egu=1.0, last_raw_des_val_steps=1000,
                 last_rel_value_egu=0.0, last_spmg=3,
                 last_user_des_val_egu=1.0, last_val_monitored=0.0,
                 last_value_archived=0.0, limit_violation=0, monitor_mask=0.0,
                 monitor_mask_more=0.0, motion_in_progress=0, motor_status=2.0,
                 motor_is_moving=0, post_process_command=0,
                 ran_out_of_retries=0, raw_desired_value_step=1000,
                 raw_encoder_position=1000, raw_high_limit_switch=0,
                 raw_low_limit_switch=0, raw_motor_position=1000,
                 raw_readback_value=1000, raw_cmnd_direction=0,
                 relative_value_egu=0.0, retry_count=0, set_set_mode=0,
                 set_use_mode=0, set_use_switch=0, stop=0,
                 stop_pause_move_go=3, sync_position=0, tweak_motor_forward=0,
                 tweak_motor_reverse=0, user_high_limit=100.0,
                 user_high_limit_switch=0, user_low_limit=-100.0,
                 user_low_limit_switch=0, user_offset_egu=0.0,
                 user_readback_value=1.0, variable_offset=0,
                 archive_deadband=0.0, bl_distance_egu=0.0,
                 bl_seconds_to_velocity=0.2, bl_speed_rps=0.5,
                 bl_velocity_egu_s=0.1, base_speed_rps=0.05,
                 base_velocity_egu_s=0.010000000000000002, dmov_input_link='',
                 derivative_gain=0.0, desired_output_loc='',
                 dial_high_limit=100.0, dial_low_limit=-100.0,
                 display_precision=3, done_moving_to_value=1,
                 egu_s_per_revolution=0.2, enable_control=0,
                 encoder_step_size_egu=0.001, engineering_units='deg',
                 hw_limit_violation_svr=0, high_alarm_limit_egu=0.0,
                 high_operating_range=0.0, high_severity=0,
                 hihi_alarm_limit_egu=0.0, hihi_severity=0,
                 home_velocity_egu_s=0.1, integral_gain=0.0,
                 jog_accel_egu_s_2=5.0, jog_velocity_egu_s=1.0,
                 lolo_alarm_limit_egu=0.0, lolo_severity=0,
                 low_alarm_limit_egu=0.0, low_operating_range=0.0,
                 low_severity=0, max_retry_count=10, max_speed_rps=0.0, max_velocity_egu_s=0.0,
                 monitor_deadband=0.0, motor_step_size_egu=0.001, move_fraction=1.0,
                 ntm_deadband_factor=2, new_target_monitor=1, offset_freeze_switch=0,
                 output_mode_select=0, output_specification='@asyn(motorSim1,0)',
                 post_move_commands='', pre_move_commands='', proportional_gain=0.0,
                 rmp_input_link='', raw_velocity=0, readback_location='', readback_outlink='',
                 readback_step_size_egu=0.0, readback_settle_time_s=0.0,
                 retry_deadband_egu=0.001, retry_mode=0, stop_outlink='',
                 seconds_to_velocity=0.2, soft_channel_position_lock=0,
                 speed_revolutions_sec=0.5, startup_commands='', status_update=0,
                 steps_per_revolution=200, tweak_step_size_egu=1.0, use_encoder_if_present=0,
                 use_rdbl_link_if_presen=0, user_direction=0, velocity_egu_s=0.1)
```
