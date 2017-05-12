import os
import graphviz

from recordwhat.parsers.st_cmd import load_records
from recordwhat.util import (fake_epics_environment, LocalRecordRegistry)
from recordwhat.graph import graph_links_with_text


test_path = os.path.split(os.path.abspath(__file__))[0]
test_ioc_path = os.path.join(test_path, 'test_ioc')


def test_local_links():
    pv_dict = load_records(fn=os.path.join(test_ioc_path, 'st.cmd'),
                           start_path=test_ioc_path,
                           )
    reg = LocalRecordRegistry(pv_dict)

    graph = graphviz.Digraph(format='pdf')

    pvs = []
    for related in reg.find_all_related_pvs(['PREFIX:ai-0']):
        pvs.append(related)

    with fake_epics_environment(reg):
        # graph = graph_links_with_subgraphs(*pvs)
        graph = graph_links_with_text(*pvs)

    # print('rendered graph to', graph.render(graph_fn))
