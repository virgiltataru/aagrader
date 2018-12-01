from enum import Enum


class Status(Enum):
    IN_PROGRESS = 0
    OK = 1
    COMPILE_ERROR = 2
    RUNTIME_ERROR = 3
    TIMEOUT = 3
    ENV_CRASH = 4


class ProgrammingLanguage(Enum):
    C = "C"
    CPP = "C++"
    PYTHON = "Python 3"



class Submission:
    def __init__(self):
        self.hw_id = None
        self.student = ""
        self.source = ""
        self.programming_language = ""
        self.compile_command = []
        self.run_command = []
        self.test_cases_input = []
        self.file_extension = ""
        self.file_contents = ""


class Testcase:
    def __init__(self):
        self.id = ""
        self.input = ""
        self.file = ""
        self.timeout = 2
        self.expected_output=""
    def __repr__(self):
        return ("Id: %s, Inputs: %s" % (self.id, self.input))

class Output:
    def __init__(self):
        self.test_case_id = ""
        self.memory = 0
        self.time = 0
        self.stdout = ""
        self.stderr = ""
        self.status = Status.IN_PROGRESS

    def __repr__(self):
        return self.stdout + self.stderr
