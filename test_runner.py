from Classes import Status
from runner import run
from test_data import tc1, source_code_add_two_numbers, tc2, source_code_infinte_loop
from test_data import source_binary_search, tc3, source_linear_search
from test_data import source_code_add_numbers_from_file, file_add_two_numbers
from test_data import source_binary_search_with_error

def test_python3_add_two_numbers_code():
    out = run(source_code_add_two_numbers, "py", None, ["python3", "Source.py"], [tc1, tc2])
    print(out)
    print(out[0].stdout)
    assert '55' == out[1].stdout
    assert Status.OK == out[0].status
    print(out[0].time)
    print(out[1].time)


def test_source_search():
    out_linear = run(source_linear_search, "py", None, ["python3", "Source.py"], [tc3])
    out_binary = run(source_binary_search, "py", None, ["python3", "Source.py"], [tc3])
    print(out_linear[0].stdout)
    assert out_linear[0].stdout == out_binary[0].stdout
    print(out_linear[0].time)
    print(out_binary[0].time)

def test_add_from_file():
    out = run(source_code_add_numbers_from_file, "py", None, ["python3", "Source.py"], [tc3], file_contents = file_add_two_numbers, file_name = "input.txt")
    print(out[0].stdout)

test_add_from_file()
