from Classes import Status
from runner import run
from test_data import tc1, source_code_add_two_numbers, tc2, source_code_infinte_loop



def test_python3_add_two_numbers_code():
    out = run(source_code_add_two_numbers, "py", None, ["python3", "Source.py"], [tc1, tc2])
    print(out)
    print(out[0].stdout)
    assert '55' == out[1].stdout
    assert Status.OK == out[0].status
    print(out[0].time)
    print(out[1].time)

test_python3_add_two_numbers_code()
