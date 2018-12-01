from Classes import Submission,Output, Status, Testcase
from runner import *
#submission = Submission object
#test_cases = list of Testcase objects

def grade(submission, test_cases):
    passed, failed, error = [], [], []
    out = run(submission.source, submission.file_extension, None, ["python3", "Source.py"], test_cases)
    for i in range(len(out)):
        if out[i].status == Status.OK:
            if out[i].stdout == test_cases[i].expected_output:
                passed.append(test_cases[i])
            else:
                failed.append(test_cases[i])
        else:
            error.append(test_cases[i])
    submission = {  'hw_id': submission.hw_id,
                    'Student': submission.student,
                    'tests_compiled': len(passed) + len(failed),
                    'tests_passed': len(passed),
                    'tests_failed': len(failed),
                    'code': submission.source,
                    'compile_times': [i.time for i in out]
            }
    return submission
