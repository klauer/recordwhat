import os
import pytest

import recordwhat
from recordwhat.areadetector import graph_ports_by_prefix

from recordwhat.areadetector import (get_plugins_by_prefix_list,
                                     get_port_dictionary)
from recordwhat.graph import port_graph

from .util import skip_if_pv_unavailable


prefix = 'XF:31IDA-BI{Cam:Tbl}'


def setup_module(module):
    test_path = os.path.split(os.path.abspath(__file__))[0]
    print('grep path is', test_path)
    recordwhat.util.default_grep_path = os.path.join(test_path, '*.dbl')


@pytest.fixture(scope='module')
def grep_tool():
    grep_tool = '/bin/grep'
    if not os.path.exists(grep_tool):
        grep_tool = '/usr/bin/grep'
    return grep_tool


def test_grep_pvs(grep_tool):
    pvs = list(recordwhat.util.grep_pvs('image1:MinCallbackTime_RBV$',
                                        ignore_exceptions=False,
                                        grep_tool=grep_tool))

    assert len(pvs) == 1

    assert not list(recordwhat.util.grep_pvs('foobarrr', grep_tool=grep_tool))


def test_port_graph():
    skip_if_pv_unavailable(prefix + 'cam1:AcquirePeriod')

    # simple way just by specifying prefix
    graph_ports_by_prefix(prefix)

    # or with more control
    plugins = get_plugins_by_prefix_list([prefix + 'TIFF1:', ])
    ad_ports = get_port_dictionary(plugins)
    port_graph(ad_ports)
