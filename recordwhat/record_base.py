from ophyd import (Device, EpicsSignal, EpicsSignalRO, Component,
                   DynamicDeviceComponent as DDC)
from .record_info import load_info_file


def _strip_field(field):
    '''Strip leading . and optional final modifier $ from a field'''
    return field.lstrip('.').rstrip('$')


class FieldComponent(Component):
    # store the per-class metadata here (class-level)
    _cls_metadata = {}

    def create_component(self, instance):
        # called when creating a component instance (i.e., field signal) on a
        # device instance (record instance)
        cpt_inst = super().create_component(instance)

        # tack on metadata to the signal instance
        record_cls = instance.__class__
        try:
            metadata = FieldComponent._cls_metadata[record_cls]
        except KeyError:
            try:
                metadata = dict(record_cls.field_metadata())
            except Exception:
                metadata = {}
            else:
                FieldComponent._cls_metadata[record_cls] = metadata

        cpt_inst.metadata = metadata.get(self.attr, None)
        return cpt_inst


FieldCpt = FieldComponent


class RecordBase(Device):
    alarm_acknowledge_severity = FieldCpt(EpicsSignalRO, '.ACKS')
    alarm_acknowledge_transient = FieldCpt(EpicsSignalRO, '.ACKT')
    access_security_group = FieldCpt(EpicsSignal, '.ASG')
    description = FieldCpt(EpicsSignal, '.DESC')
    scan_disable_input_link_value = FieldCpt(EpicsSignal, '.DISA')
    disable_putfields = FieldCpt(EpicsSignal, '.DISP')
    disable_alarm_severity = FieldCpt(EpicsSignal, '.DISS')
    disable_value = FieldCpt(EpicsSignal, '.DISV')
    device_type = FieldCpt(EpicsSignal, '.DTYP')
    event_number = FieldCpt(EpicsSignal, '.EVNT')
    forward_link = FieldCpt(EpicsSignal, '.FLNK$')
    lock_count = FieldCpt(EpicsSignalRO, '.LCNT')
    record_name = FieldCpt(EpicsSignalRO, '.NAME$')
    new_alarm_severity = FieldCpt(EpicsSignalRO, '.NSEV')
    new_alarm_status = FieldCpt(EpicsSignalRO, '.NSTA')
    processing_active = FieldCpt(EpicsSignalRO, '.PACT')
    scan_phase_number = FieldCpt(EpicsSignal, '.PHAS')
    process_at_initialization = FieldCpt(EpicsSignal, '.PINI')
    priority = FieldCpt(EpicsSignal, '.PRIO')
    process_record = FieldCpt(EpicsSignal, '.PROC')
    dbputfield_process = FieldCpt(EpicsSignalRO, '.PUTF')
    reprocess = FieldCpt(EpicsSignalRO, '.RPRO')
    scanning_rate = FieldCpt(EpicsSignal, '.SCAN')
    scan_disable_input_link = FieldCpt(EpicsSignal, '.SDIS$')
    current_alarm_severity = FieldCpt(EpicsSignalRO, '.SEVR')
    trace_processing = FieldCpt(EpicsSignal, '.TPRO')
    time_stamp_event = FieldCpt(EpicsSignal, '.TSE')
    time_stamp_event_link = FieldCpt(EpicsSignal, '.TSEL$')
    val_undefined = FieldCpt(EpicsSignal, '.UDF')
    value = FieldCpt(EpicsSignal, '.VAL')

    @classmethod
    def field_metadata(cls):
        if not hasattr(cls, '_rtyp'):
            raise ValueError('No associated record type')

        rtyp = cls._rtyp

        field_to_md = load_info_file(rtyp)
        for attr, suffix, cpt in cls._record_attr_components():
            if suffix in field_to_md:
                yield attr, field_to_md[suffix]

    @classmethod
    def attrs_of_type(cls, epics_type):
        if isinstance(epics_type, str):
            for attr, md in cls.field_metadata():
                if md.type == epics_type:
                    yield attr
        else:
            for attr, md in cls.field_metadata():
                if md.type in epics_type:
                    yield attr

    @classmethod
    def attr_to_field(cls, attr):
        return cls._sig_attrs[attr].suffix.lstrip('.')

    @classmethod
    def _record_attr_components(cls):
        for attr, cpt in cls._sig_attrs.items():
            if isinstance(cpt, DDC):
                for sub_attr, (_, suffix, _) in cpt.defn.items():
                    suffix = _strip_field(suffix)
                    yield '{}.{}'.format(cpt.attr, sub_attr), suffix, cpt
            else:
                suffix = _strip_field(cpt.suffix)
                yield attr, suffix, cpt

    @classmethod
    def field_to_attr(cls, field):
        for attr, suffix, cpt in cls._record_attr_components():
            if suffix == field:
                return attr
