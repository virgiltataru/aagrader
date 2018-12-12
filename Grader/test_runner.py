from Classes import Status, Submission
from runner import run_source
from test_data import tc1, source_code_add_two_numbers, tc2, source_code_infinte_loop
from test_data import source_binary_search, tc3, source_linear_search
from test_data import source_code_add_numbers_from_file, file_add_two_numbers
from test_data import source_binary_search_with_error
from pymongo import MongoClient
from check_similarity import check_similarity

def test_python3_add_two_numbers_code():
    out = run_source(source_code_add_two_numbers, "py", None, ["python3", "Source.py"], [tc1, tc2])
    print(out)
    assert tc1.expected_output == out[0].stdout
    assert Status.OK == out[0].status
    print(out[0].time)
    print(out[1])
    passed, failed =[], []
    for output in out:
        if output.status == Status.OK:
            passed.append(out)
        else:
            failed.append(out)
    submission = {
                'Student': 'Edwin',
                'tests_passed': len(passed),
                'tests_failed': len(failed)
        }
    client = MongoClient()
    db = client.submissions
    db.submissions.insert_one(submission)
    print(db.submissions.find_one({'tests_passed': 2}))
    db.submissions.drop()



def test_source_search():
    out_linear = run_source(source_linear_search, "py", None, ["python3", "Source.py"], [tc3])
    out_binary = run_source(source_binary_search, "py", None, ["python3", "Source.py"], [tc3])
    print(out_linear[0].stdout)
    assert out_linear[0].stdout == out_binary[0].stdout
    print(out_linear[0].time)
    print(out_binary[0].time)
def test_add_from_file():
    out = run_source(source_code_add_numbers_from_file, "py", None, ["python3", "Source.py"], [tc3], file_contents = file_add_two_numbers, file_name = "input.txt")
    print(out[0].stdout)

def test_timeout():
    out = run_source(source_binary_search_with_error, "py", None, ["python3", "Source.py"], [tc3], file_contents = file_add_two_numbers, file_name = "input.txt")
    print(out[0])
#returned http://moss.stanford.edu/results/577007998
def test_similarity():
    submission_1 = {
                'hw_id': 1,
                'Student': 'Edwin',
                'tests_passed': 2,
                'tests_failed': 3,
                'code': source_linear_search
        }
    submission_2 = {
                'hw_id': 1,
                'Student': 'Alex',
                'tests_passed': 3,
                'tests_failed': 2,
                'code': source_binary_search
    }

    submission_3 ={
                'hw_id': 1,
                'Student': 'Julius',
                'tests_passed': 5,
                'tests_failed': 2,
                'code': source_binary_search

    }
    client = MongoClient()
    db = client.submissions
    db.submissions.insert_one(submission_1)
    db.submissions.insert_one(submission_2)
    db.submissions.insert_one(submission_3)
    print(check_similarity(1))
    db.submissions.drop()
