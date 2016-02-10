import recordwhat

rec = recordwhat.get_record_by_name('XF:31IDA-OP{Tbl-Ax:X1}Mtr', read_attrs=[])

# get a specific field's value
print('steps_per_revolution =', rec.steps_per_revolution.get())

# or access to the signal itself
print('steps_per_revolution signal =', rec.steps_per_revolution)
print()

# or ask for *all* the values
print(rec.get())
