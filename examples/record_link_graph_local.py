import sys
from collections import OrderedDict

import graphviz

from recordwhat.graph import (graph_links_with_subgraphs,
                              graph_links_with_text)
from recordwhat.parsers.st_cmd import load_records

from recordwhat.util import (fake_epics_environment, LocalRecordRegistry)


def main(pvs, *, graph_fn='graph',
         st_cmd='/Users/klauer/iocs/hgvpu-current/iocBoot/ioc-und1-uc01/st.cmd',
         start_path='/Users/klauer/iocs/hgvpu-current/iocBoot/ioc-und1-uc01/'):
    import logging
    logging.getLogger('recordwhat.graph').setLevel(logging.DEBUG)
    logging.basicConfig()

    reg = LocalRecordRegistry(load_records(fn=st_cmd, start_path=start_path))
    print('total loaded', len(reg.pvs), 'records', len(list(reg.records)))
    print()
    print()
    graph = graphviz.Digraph(format='pdf')

    for related in reg.find_all_related_pvs(pvs):
        pvs.append(related)

    with fake_epics_environment(reg):
        # graph = graph_links_with_subgraphs(*pvs)
        graph = graph_links_with_text(*pvs)

    print('rendered graph to', graph.render(graph_fn))
    return graph


if __name__ == '__main__':
    pvs = list(sys.argv[1:])
    if not pvs:
        print('Usage {} [pvs]'.format(sys.argv[0]))
        sys.exit(1)

    main(pvs)
