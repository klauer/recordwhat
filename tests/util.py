import pytest
import epics


def skip_if_pv_unavailable(pvname):
    pv = epics.PV(pvname)
    pv.wait_for_connection(0.2)
    if not pv.connected:
        raise pytest.skip('pv {} unavailable'.format(pvname))
