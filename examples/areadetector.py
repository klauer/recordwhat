from recordwhat.areadetector import graph_ports_by_prefix

from recordwhat.areadetector import (get_plugins_by_prefix_list,
                                     get_port_dictionary)
from recordwhat.graph import port_graph


# Detector prefix:
prefix = 'XF:03IDC-ES{Tpx:1}'
# Save to this without svg extension:
save_to = 'ad_ports'

# simple way just by specifying prefix
graph1 = graph_ports_by_prefix(prefix)
print('Saved to', graph1.render(save_to))


if False:
    # or with more control
    plugins = get_plugins_by_prefix_list([prefix + 'TIFF1:',
                                          ]
                                         )
    ad_ports = get_port_dictionary(plugins)
    graph2 = port_graph(ad_ports)
