from parsimonious.grammar import Grammar, NodeVisitor
from collections import OrderedDict
import os.path
import attr

dbd_grammar = Grammar(r"""
dbd = db_entry*
db_entry = (comment / cimport / field / menu / record_type /
            variable / device / include / registrar /
            function / driver / "\n")

field = _ "field(" f_name "," _ f_type ")" _ "{" field_body _  "}"
field_body = fp*
f_name = ~"[A-Z0-9_]+"
f_type = ("DBF_STRING" / "DBF_CHAR" / "DBF_UCHAR" /
          "DBF_SHORT" / "DBF_USHORT" / "DBF_LONG" / "DBF_ULONG" /
          "DBF_FLOAT" / "DBF_DOUBLE" / "DBF_ENUM" / "DBF_MENU" /
          "DBF_DEVICE" / "DBF_INLINK" / "DBF_OUTLINK" / "DBF_FWDLINK" /
          "DBF_NOACCESS")
fp = _ (g_field / prompt / special / size / promptgroup /
        comment / extra / "\n")
g_field = g_f_name "(" g_f_body ")\n"

prompt = "prompt(" prompt_val ")\n"
special = "special(" special_val ")\n"
size = "size(" size_val ")\n"
extra = "extra(" extra_val ")\n"
promptgroup = "promptgroup(" promptgroup_val ")\n"

g_f_name = ~"[a-z]*"
g_f_body = ~"[^)]*"
prompt_val = ~'"[^"]*"'
extra_val = ~'"[^"]*"'
promptgroup_val = ~'"[^"]*"'
special_val = ~'[^)]*'
size_val = ~'[0-9]*'

menu = "menu(" menu_name ")" _ "{" (choice / comment / "\n")* "}" "\n"
choice = _ "choice(" ~"[^,]*" "," _ ~'"[^"]*"' ")\n"
menu_name = ~"[a-z0-9]*"i

record_type = "recordtype(" rec_name ")" _ "{" (field / include /
                                                cimport / comment / "\n")* "}"
include = _ "include" _ include_fname _
include_fname = ~'"[^"]*"'
rec_name = ~"[a-z]*"i
_ = ~r"\s*"

variable = "variable("  ~"[^)]*" ")"
device = "device" _ "(" ~"[^)]*" ")"
registrar = "registrar(" ~"[^)]*" ")"
function = "function" _ "(" ~"[^)]*" ")"
driver = "driver(" ~"[^)]*" ")"

cimport = ~"\s*%[^\r\n]*"
comment = ~"\s*#[^\r\n]*"

""")


@attr.s(frozen=True)
class dbdField:
    name = attr.ib()
    dbf_type = attr.ib()

    asl = attr.ib(default='', repr=False)
    initial = attr.ib(default='', repr=False)
    promptgroup = attr.ib(default='', repr=False)
    prompt = attr.ib(default='', repr=False)
    special = attr.ib(default='', repr=False)
    pp = attr.ib(default='', repr=False)
    interest = attr.ib(default='', repr=False)
    base = attr.ib(default='', repr=False)
    size = attr.ib(default='', repr=False)
    extra = attr.ib(default='', repr=False)
    menu = attr.ib(default='', repr=False)
    # this is undocumented, but in lots of dbd in epics-base
    prop = attr.ib(default='', repr=False)


@attr.s(frozen=True)
class dbdRecordType:
    name = attr.ib()
    fields = attr.ib()


class RecordWalker(NodeVisitor):
    def __init__(self, *, out_path='/tmp'):
        self.out_path = out_path

    def visit_dbd(self, node, visited_children):
        records = [c for c in visited_children
                   if isinstance(c, dbdRecordType)]

        return {r.name: r for r in records}

    def visit_db_entry(self, node, visited_children):
        return visited_children[0]

    def visit_field(self, node, visited_children):
        (_ws, _kw, f_name, _cm, _ws, f_type, _rp, _ws, _lc,
         fp, _ws, _rc) = visited_children
        fp = [c[0] for c in fp if c[0] is not None]
        return dbdField(name=f_name, dbf_type=f_type,
                        **{k: v for (k, v) in fp})

    def visit_f_name(self, node, visited_children):
        return node.text

    def visit_field_body(self, node, visited_children):
        return visited_children

    def visit_f_type(self, node, visited_children):
        return node.text

    def visit_g_f_name(self, node, visited_children):
        return node.text

    def visit_g_f_body(self, node, visited_children):
        return node.text

    def visit_fp(self, node, visited_children):
        _ws, p = visited_children
        return p

    def visit_prompt(self, node, visited_children):
        _, pv, *_ = visited_children
        return ('prompt', pv)

    def visit_special(self, node, visited_children):
        _, sz, _ = visited_children
        return ('special', sz)

    def visit_size(self, node, visited_children):
        _, sz, _ = visited_children
        return ('size', sz)

    def visit_extra(self, node, visited_children):
        ...

    def visit_g_field(self, node, visited_children):
        g_nm, _lp, g_b, _rp = visited_children
        return (g_nm, g_b)

    def visit_promptgroup(self, node, visited_children):
        ...

    def visit_prompt_val(self, node, visited_children):
        return node.text

    def visit_extra_val(self, node, visited_children):
        ...

    def visit_promptgroup_val(self, node, visited_children):
        ...

    def visit_special_val(self, node, visited_children):
        ...

    def visit_size_val(self, node, visited_children):
        ...

    def visit_menu(self, node, visited_children):
        ...

    def visit_choice(self, node, visited_children):
        ...

    def visit_menu_name(self, node, visited_children):
        ...

    def visit_record_type(self, node, visited_children):
        _kw, name, _rp, _ws, _lc, innards, _rc = visited_children
        fields = [c[0] for c in innards
                  if isinstance(c[0], dbdField)]
        fields = OrderedDict((f.name, f) for f in fields)

        return dbdRecordType(name=name, fields=fields)

    def visit_include(self, node, visited_children):
        ...

    def visit_include_fname(self, node, visited_children):
        ...

    def visit_rec_name(self, node, visited_children):
        return node.text

    def visit__(self, node, visited_children):
        ...

    def visit_variable(self, node, visited_children):
        ...

    def visit_device(self, node, visited_children):
        ...

    def visit_registrar(self, node, visited_children):
        ...

    def visit_function(self, node, visited_children):
        ...

    def visit_driver(self, node, visited_children):
        ...

    def visit_cimport(self, node, visited_children):
        ...

    def visit_comment(self, node, visited_children):
        ...

    def visit_catchall(self, node, visited_children):
        ...

    def visit_(self, node, visited_children):
        return visited_children


def write_table(out_path, record):
    '''Write file of meta-data as created by dbd.py

    Creates a file called NAME.txt

    Parameters
    ----------
    out_path : str
        Path to write the file to

    record : dbdRecordType
        The record to write to disk
    '''
    columns = ['field', 'type', 'asl', 'initial', 'promptgroup',
               'prompt', 'special', 'pp', 'interest', 'base', 'size',
               'extra', 'menu']

    fn = os.path.join(out_path, '{}.txt'.format(record.name))
    with open(fn, 'w') as fout:
        print('\t'.join(columns), file=fout)
        for f in record.fields.values():
            row = [f.name, f.dbf_type] + [getattr(f, k) for k in columns[2:]]
            print('\t'.join(row), file=fout)
