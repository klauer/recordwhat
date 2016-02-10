from recordwhat.graph import graph_links

# a single record
# graph = graph_links('XF:31IDA-OP{Tbl-Ax:FakeMtr}-SP_')

# a number of records in one diagram:
graph = graph_links('XF:03IDC-ES{SPod:1}Move-Cmd',
                    'XF:03IDC-ES{SPod:1}Move-Cmd_',
                    'XF:03IDC-ES{SPod:1}Moving-I_',
                    'XF:03IDC-ES{SPod:1}MovingRaw-I_',
                    'XF:03IDC-ES{SPod:1}Moving-I',
                    'XF:03IDC-ES{SPod:1}Move-Seq_',
                    'XF:03IDC-ES{SPod:1}BusyMoving_',
                    )

# (output provided in repo, since chances are you don't have a smarpod IOC
# running)
print('rendered graph to', graph.render('record_link_graph'))
