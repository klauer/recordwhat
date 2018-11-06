from collections import OrderedDict
from parsimonious.grammar import Grammar, NodeVisitor
import attr
from inspect import Parameter, Signature

template_grammar = Grammar(r"""
str = part*
part = (template / template_curly / literal)
template = tmp_l tmp_c tmp_r
template_curly = tmp_l_curly tmp_c_curly tmp_r_curly
tmp_l = "$" !"$" "("
tmp_l_curly = "$" !"$" "{"
tmp_c = tmp_name tmp_dflt
tmp_c_curly = tmp_name_curly tmp_dflt_curly
tmp_name =  ~"[^),=]*"
tmp_dflt = ~"[,=][^)]*"?
tmp_name_curly =  ~"[^},=]*"
tmp_dflt_curly = ~"[,=][^}]*"?
tmp_r = ")"
tmp_r_curly = "}"
literal = ( ~"[^$]*")
""")


@attr.s
class Template:
    val = attr.ib()
    sig = attr.ib()
    fmt_func = attr.ib()


class TemplateWalker(NodeVisitor):
    def visit_str(self, node, visited_children):
        parameters = []
        out = []
        for typ, val, key in visited_children:
            if typ == 'T':
                key, dflt = key
                parameters.append(Parameter(name=key,
                                            kind=Parameter.KEYWORD_ONLY,
                                            default=dflt, annotation=str))
            out.append(val)

        template = ''.join(out)
        sig = Signature(parameters, return_annotation=str)

        def format(**kwargs):
            b = sig.bind(**kwargs)
            b.apply_defaults()
            return template.format(**b.kwargs)

        return Template(val=template, sig=sig, fmt_func=format)

    def visit_part(self, node, visited_children):
        child, = visited_children
        return child

    def visit_template(self, node, visited_children):
        _, (name, dflt), _ = visited_children
        return 'T', '{{{}}}'.format(name), (name, dflt)

    visit_template_curly = visit_template

    def _base(self, node, visited_children):
        return node.text

    visit_tmp_l = visit_tmp_r = _base
    visit_tmp_name = visit_tmp_name_curly = _base
    visit_tmp_l_curly = visit_tmp_r_curly = _base

    def visit_tmp_dflt(self, node, visited_children):
        if node.text:
            return node.text[1:]
        return Parameter.empty

    visit_tmp_dflt_curly = visit_tmp_dflt

    def visit_tmp_c(self, node, visited_children):
        return visited_children

    visit_tmp_c_curly = visit_tmp_c

    def visit_literal(self, node, visited_children):
        return 'L', node.text.replace('{', '{{').replace('}', '}}'), None

    def visit_(self, node, visited_children):
        return node.text


db_grammar = Grammar(r"""
db = (comment / record / include / free_alias / "\n")+
record = ( _ ("grecord" / "record") _ "(" _ ) rtype "," _ pv_name ")" _ "{" r_entry* "}"
rtype = ~"[a-z]*"i
r_entry = (field / alias / info / comment / include / "\n" / _)

field = _ ("field" _ "(" _) f_name (_ ",") _ f_val (_ ")" _ comment?)
alias = _ ("alias" _ "(" _) a_name ")"
info = _ ("info" _ "(" _) i_name "," _ i_val (_ ")")

free_alias = _ ("alias" _ "(") a_name (_ "," _ ) a_name ")"

f_val = (~'"[^"]*"' / ~'[^)]*')
i_val = ~'[^)]*'

pv_name = (~'"[^"]*"' / ~'[^)]*')

f_name = ~"[A-Z0-9]*"i
a_name = (~'"[^"]*"' / ~'[^)]*')
i_name = (~"[A-Z0-9:_]*"i / ~'"[^"]*"')

comment = ~"\s*#[^\r\n]*"

include = _ "include" _ include_fname _
include_fname = ~'"[^"]*"'

_ = ~r"\s*"
""")


@attr.s
class dbRecord:
    rtype = attr.ib()
    pvname = attr.ib()
    fields = attr.ib()
    info = attr.ib(default=attr.Factory(OrderedDict))
    alias = attr.ib(default=attr.Factory(list))


@attr.s
class dbField:
    name = attr.ib()
    value = attr.ib()


@attr.s
class dbInfo:
    name = attr.ib()
    value = attr.ib()


@attr.s
class dbAlais:
    name = attr.ib()


class dbWalker(NodeVisitor):

    def visit_db(self, node, visited_children):
        records = [c[0] for c in visited_children
                   if isinstance(c[0], dbRecord)]
        return records

    def visit_record(self, node, visited_children):
        (_kw, rtype, _cm, _ws, pv_name, _rp, _ws,
         _lb, r_entry, _rb) = visited_children
        fields = OrderedDict(((f.name, f) for f in r_entry
                              if isinstance(f, dbField)))
        info = OrderedDict(((i.name,  i) for i in r_entry
                            if isinstance(i, dbInfo)))
        return dbRecord(rtype=rtype, pvname=pv_name, fields=fields, info=info)

    def visit_pv_name(self, node, visited_children):
        return node.text

    def visit_rtype(self, node, visited_children):
        return node.text

    def visit_r_entry(self, node, visited_children):
        return visited_children[0]

    def visit_field(self, node, visited_children):
        _ws, _kw, f_name, _cm, _ws, f_val, _rp = visited_children
        return dbField(name=f_name, value=f_val)

    def visit_info(self, node, visited_children):
        _ws, _kw, i_name, _cm, _ws, i_val, _rp = visited_children
        return dbInfo(name=i_name, value=i_val)

    def visit_alias(self, node, visited_children):
        _ws, _kw, a_name, _rp = visited_children
        return dbAlais(name=a_name)

    def visit_free_alias(self, node, visited_children):
        ...

    def visit_f_val(self, node, visited_children):
        return node.text

    def visit_i_val(self, node, visited_children):
        return node.text

    def visit_f_name(self, node, visited_children):
        return node.text

    def visit_a_name(self, node, visited_children):
        return node.text

    def visit_i_name(self, node, visited_children):
        return node.text

    def visit__(self, node, visited_children):
        ...

    def visit_comment(self, node, visited_children):
        ...

    def visit_(self, node, visited_children):
        return visited_children

    def visit_include_fname(self, node, visited_children):
        return node.text

    def visit_include(self, node, visited_children):
        ...
