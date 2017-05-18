from recordwhat.parsers.db_parsimonious import template_grammar, TemplateWalker
import pytest


@pytest.fixture
def tw():
    return TemplateWalker()


@pytest.mark.parametrize('template,kwargs,expected', [
    # dead simple
    ('abc$(foo)def', {'foo': 'BAR'}, 'abcBARdef'),
    # escape {}
    ('abc{$(foo)}def', {'foo': 'BAR'}, 'abc{BAR}def'),
    ('abc{{$(foo)}}def', {'foo': 'BAR'}, 'abc{{BAR}}def'),
    # default values
    ('abc$(foo,def)', {}, 'abcdef'),
    ('abc$(foo,)', {}, 'abc'),
    ('abc$(foo=def)', {}, 'abcdef'),
    ('abc$(foo=)', {}, 'abc'),

    # dead simple
    ('abc${foo}def', {'foo': 'BAR'}, 'abcBARdef'),
    # escape {}
    ('abc{${foo}}def', {'foo': 'BAR'}, 'abc{BAR}def'),
    ('abc{{${foo}}}def', {'foo': 'BAR'}, 'abc{{BAR}}def'),
    # default values
    ('abc${foo,def}', {}, 'abcdef'),
    ('abc${foo,}', {}, 'abc'),
    ('abc${foo=def}', {}, 'abcdef'),
    ('abc${foo=}', {}, 'abc'),
])
def test_templates(tw, template, kwargs, expected):
    T = tw.visit(template_grammar.parse(template))
    assert T.fmt_func(**kwargs) == expected
