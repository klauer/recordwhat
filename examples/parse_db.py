from recordwhat.parsers.db_parsimonious import (
    db_grammar, dbWalker, template_grammar, TemplateWalker)
from recordwhat.util import read_file
from pathlib import Path


def ingest_db_file(fname, root):
    dw = dbWalker()
    return dw.visit(db_grammar.parse(read_file(fname, path=str(root))))


def stream_components(recs, nm_maker):
    tw = TemplateWalker()

    for r in recs:
        rtype = r.rtype
        pv_template = tw.visit(template_grammar.parse(r.pvname))
        pv = pv_template.val.format(**{k: ''
                                       for k in pv_template.sig.parameters})
        nm = nm_maker(pv)
        yield '{} = Cpt({}, {})'.format(nm, rtype, pv)


root = Path('epics/areadetector/areaDetector/ADCore/ADApp/Db')
recs = ingest_db_file(root / 'NDArrayBase.template', root)
for l in stream_components(recs, str.lower):
    print(f'    {l}')
