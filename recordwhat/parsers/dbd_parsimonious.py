from parsimonious.grammar import Grammar, NodeVisitor

dbd_grammer = Grammar(r"""
dbd = (comment / cimport / field / menu / record_type /
       variable / device / include / registrar /
       function / driver / "\n")+

field = _ "field(" f_name "," _ f_type ")" _ "{" (fp / "\n" )* _  "}"
f_name = ~"[A-Z0-9_]+"
f_type = ("DBF_STRING" / "DBF_CHAR" / "DBF_UCHAR" /
          "DBF_SHORT" / "DBF_USHORT" / "DBF_LONG" / "DBF_ULONG" /
          "DBF_FLOAT" / "DBF_DOUBLE" / "DBF_ENUM" / "DBF_MENU" /
          "DBF_DEVICE" / "DBF_INLINK" / "DBF_OUTLINK" / "DBF_FWDLINK" /
          "DBF_NOACCESS")
fp = _ (prompt / special / size / promptgroup /
        g_field / comment / extra / "\n")
prompt = "prompt(" prompt_val ")\n"
special = "special(" special_val ")\n"
size = "size(" size_val ")\n"
extra = "extra(" extra_val ")\n"
g_field = ~"[a-z]*\(" ~"[^)]*" ")\n"
promptgroup = "promptgroup(" promptgroup_val ")\n"
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


class OphydMaker(NodeVisitor):

    def visit_dbd(self, node, visited_children):
        ...

    def visit_field(self, node, visited_children):
        ...

    def visit_f_name(self, node, visited_children):
        ...

    def visit_f_type(self, node, visited_children):
        ...

    def visit_fp(self, node, visited_children):
        ...

    def visit_prompt(self, node, visited_children):
        ...

    def visit_special(self, node, visited_children):
        ...

    def visit_size(self, node, visited_children):
        ...

    def visit_extra(self, node, visited_children):
        ...

    def visit_g_field(self, node, visited_children):
        ...

    def visit_promptgroup(self, node, visited_children):
        ...

    def visit_prompt_val(self, node, visited_children):
        ...

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
        ...

    def visit_include(self, node, visited_children):
        ...

    def visit_include_fname(self, node, visited_children):
        ...

    def visit_rec_name(self, node, visited_children):
        ...

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
        ...
