[![Build Status](https://travis-ci.org/virgiltataru/aagrader.svg?branch=master)](https://travis-ci.org/virgiltataru/aagrader)

# auto-grader

> #### Autograder for NYU.

To run
- source env/bin/activate
- Go to Grader folder
- run: python api.py
- to post json
{"test": [1,2],
"code":"",
"code_file": "code_file",
"extension": "py",
"test_input": [],
"test_input_files": ["test1", "test1"],
"test_output":["35"],
"student": "Brad",
"assignment_id": 111,
"pass_req": 1,
"max_lines": 5
}

Tech Stack:

- Backend - Django
- Frontend - Vue ?
- Sandbox - C
- Pymongo (https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb)
- Roadmap

- Autograder
- API to communicate with other web service
  - jsonify to convert
  - something else to convert the json object back in to a dictionary
- security
- Analytics for the teacher

- Other web service
  - front-end: Mathew is working

App's overview

- login/ register page
- flow
  - semesters
    - each semester has courses
      - each course has assignments.
      - each course has students. - each assignment for each student has submissions.
- Admin
  - add - semesters. - courses - assignments.
    students
  - can only over

models

- Users
- Semesters
- courses
- Assignment
- Enrolment - contains information about who is enrolled and in which course
- submissions - contains information about the submissions done by each student.


mongodb is used instead of sqlite
Matthew will work on the front-end this weekend
API is ready
