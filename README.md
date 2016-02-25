recordwhat
==========

Selection of utilities for poking around with EPICS records

* `ophyd.Device`s for most EPICS record types with sensible attribute names
* Give a record name, get a device instance for that record

With the help of graphviz
* Graph record input, output, and forward links
* Graph areaDetector port plugin sources

Record in/out/forward link graphing
-----------------------------------
![Record link graph example](https://cdn.rawgit.com/klauer/recordwhat/0.3/examples/record_link_graph.svg)
[Source](examples/record_link_graph.py)

AreaDetector port graphing
--------------------------
![Port mapping example](https://cdn.rawgit.com/klauer/recordwhat/0.3/examples/ad_ports.svg)
[Source](examples/areadetector.py)

Record example
--------------

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
[Full source](examples/motor.py)


Output:
```python
steps_per_revolution = 200
steps_per_revolution signal = EpicsSignal(read_pv='XF:31IDA-OP{Tbl-Ax:X1}Mtr.SREV', 
                                          parent='XF:31IDA-OP{Tbl-Ax:X1}Mtr', value=200, 
                                          timestamp=1455045145.501072, pv_kw={}, auto_monitor=False, 
                                          string=False, write_pv='XF:31IDA-OP{Tbl-Ax:X1}Mtr.SREV',
                                          limits=False, put_complete=False)

MotorRecordTuple(alarm_acknowledge_severity=0, alarm_acknowledge_transient=1,
                 access_security_group='', description='Delta',
                 scan_disable_input_link_value=0, disable_putfields=0,

                 # (... a bunch of lines clipped...)

                 seconds_to_velocity=0.2, soft_channel_position_lock=0,
                 speed_revolutions_sec=0.5, startup_commands='', status_update=0,
                 steps_per_revolution=200, tweak_step_size_egu=1.0, use_encoder_if_present=0,
                 use_rdbl_link_if_presen=0, user_direction=0, velocity_egu_s=0.1)
```

Requires
--------
* Python 3.4+
* ophyd
* pyepics
