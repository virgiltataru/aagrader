from Classes import Submission,Output, Status, Testcase

#submission = Submission object
#test_cases = list of Testcase objects

def grade(submission, test_cases):
    passed, failed, error = [], [], []
    out = run(submission.source, "py", None, ["python3", "Source.py"], test_cases)
    for i in range(len(out)):
        if out[i].status == Status.OK:
            if out[i].stdout == test_cases[i].stdout:
                passed.append(test_cases[i])
            else:
                failed.append(test_cases[i])
        else:
            error.append(test_cases[i])
    submission = {
                    'Student': submission.student,
                    'tests_compiled': len(passed) + len(failed),
                    'tests_passed': len(passed),
                    'tests_failed': len(failed),
            }
    client = MongoClient()
    db=client.submissions
    result= db.students.insert_one(submission)
