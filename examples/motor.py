import recordwhat

rec = recordwhat.get_record_by_name('XF:31IDA-OP{Tbl-Ax:X1}Mtr', read_attrs=[])

# get a specific field's value
print('steps_per_revolution =', rec.steps_per_revolution.get())

# or access to the signal itself
print('steps_per_revolution signal =', rec.steps_per_revolution)
print()

# or ask for *all* the values
print(rec.get())

# poke around with field metadata
metadata = dict(rec.field_metadata())
print('description field type', metadata['description'].type)
print('derivative gain metadata', metadata['derivative_gain'])

print('in links', list(rec.attrs_of_type('DBF_INLINK')))
print('all links', list(rec.attrs_of_type(['DBF_INLINK', 'DBF_OUTLINK',
                                           'DBF_FWDLINK'])))

from recordwhat.graph import graph_links

graph = graph_links('XF:31IDA-OP{Tbl-Ax:FakeMtr}-SP_')
# or a number of records in one diagram:
# graph = graph_links('XF:03IDC-ES{SPod:1}Move-Cmd',
#                     'XF:03IDC-ES{SPod:1}Move-Cmd_',
#                     'XF:03IDC-ES{SPod:1}Moving-I_',
#                     'XF:03IDC-ES{SPod:1}MovingRaw-I_',
#                     'XF:03IDC-ES{SPod:1}Moving-I',
#                     'XF:03IDC-ES{SPod:1}Move-Seq_',
#                     'XF:03IDC-ES{SPod:1}BusyMoving_',
#                     )




print('rendered graph to', graph.render('test'))
