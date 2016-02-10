import epics


_record_classes = {}


def _register_record_type(rtyp):
    def wrapped(cls):
        cls._rtyp = rtyp
        _record_classes[rtyp] = cls
        return cls

    return wrapped


def get_record_class(rtyp):
    try:
        return _record_classes[rtyp]
    except KeyError:
        raise ValueError('Unrecognized record type: {}'.format(rtyp))


def get_record_by_name(record_name, *, timeout=1.0, **kwargs):
    if '.' in record_name:
        record_name = record_name.split('.')[0]

    rtyp_pvname = '{}.RTYP'.format(record_name)
    record_type = epics.caget(rtyp_pvname, timeout=timeout)
    if record_type is None:
        raise TimeoutError('Timed out requesting record type')

    record_class = get_record_class(record_type)
    return record_class(record_name, **kwargs)
