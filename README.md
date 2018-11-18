# auto-grader

> #### Autograder for NYU.

Tech Stack:

- Backend - Django
- Frontend - Vue ?
- Sandbox - C


Roadmap
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
        - each course has students.
              - each assignment for each student has submissions.
- Admin
  - add
      - semesters.
      - courses
      - assignments.
students
  - can only over



models
  - Users
  - Semesters
  - courses
  - Assignment
  - Enrolment
        - contains information about who is enrolled and in which course
  - submissions
        - contains information about the submissions done by each student.
