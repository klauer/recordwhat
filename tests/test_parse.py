import os
from recordwhat.parsers.st_cmd import load_records
from recordwhat.util import LocalRecordRegistry


test_path = os.path.split(os.path.abspath(__file__))[0]
test_ioc_path = os.path.join(test_path, 'test_ioc')


def test_parse_st_cmd():
    pv_dict = load_records(fn=os.path.join(test_ioc_path, 'st.cmd'),
                           start_path=test_ioc_path,
                           )
    reg = LocalRecordRegistry(pv_dict)

    print('total loaded', len(reg.pvs), 'records', len(list(reg.records)))
    print(pv_dict)

    assert pv_dict['PREFIX:ai-0'] == '0'
    assert pv_dict['PREFIX:bi-0'] == '0'
    assert pv_dict['PREFIX:ai-1'] == '1'
    assert pv_dict['PREFIX:bi-1'] == '1'
