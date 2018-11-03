from Classes import Status
from runner import run
from test_data import tc1, python3_source_code_add_two_numbers



def test_python3_add_two_numbers_code():
    out = run(python3_source_code_add_two_numbers, "py", None, ["python3", "Source.py"], [tc1])
    print(out)
    assert 1 == len(out)
    assert '57' == out[0].stdout
    assert Status.OK == out[0].status

test_python3_add_two_numbers_code()







