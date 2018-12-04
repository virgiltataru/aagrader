'''
For documentatiion on subprocess, read here
https://docs.python.org/3/library/subprocess.html

uuid is used to generate an unique ID for all folders.
https://docs.python.org/3/library/uuid.html

@ denotes returns
'''

import subprocess
import os
import docker
import time
import uuid
import shutil

from Classes import Output, Status, Testcase

#@ array of Output objects
def run(source, source_extension, compile_commands, run_commands, test_cases=None, file_contents = None, file_name = None):
    #create a new directory where the files will be created in
    #so we can remove them easily after
    current_directory = os.getcwd()
    temp_dir = uuid.uuid4().hex
    os.makedirs(temp_dir)
    os.chdir(temp_dir)
    result = []


    try:
        #create sorce file (and text file if needed) and execute the tests
        source_file_name = create_file(source, "Source.py")
        if file_contents and file_name:
            create_text_file(file_contents, file_name)
        out_compile = compile_code(compile_commands, source_file_name, result)
        execute_tests(run_commands, test_cases, out_compile, result)
    #permission errors, environment problems, ect
    except Exception as e:
        print(os.sys.exc_info())

    #return to the original directory and remove the temp one
    os.chdir(current_directory)
    shutil.rmtree(temp_dir, True)

    return result


def execute_tests(run_command, test_cases, out_compile, result):
    if out_compile.status == Status.COMPILE_ERROR:
            return ("Compilation Error")
    else:
        #run each test case and add the output to the list
        for test_case in test_cases:
            out_test = Output()
            out_test.test_case_id = test_case.id

            if run_command:
                start_time = time.time()
                completed = subprocess.run(run_command,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           input=test_case.input.encode('utf-8'),
                                           timeout=test_case.timeout,
                                           check = True)
                out_test.stderr = completed.stderr.decode('utf-8').rstrip()
                out_test.stdout = completed.stdout.decode('utf-8').rstrip()
                out_test.time = time.time() - start_time
                if completed.returncode:
                    out_test.status = Status.RUNTIME_ERROR
                else:
                    out_test.status = Status.OK

                result.append(out_test)
            else:
                raise ValueError("Test cases must have a run command")

#Compiles source code and runs the commands on the executable
#@ Output object
def compile_code(compile_commands, source_file_name, result):
    out_compile = Output()
    if not compile_commands:
        out_compile.status = Status.OK
        return out_compile

    else:
        compile_commands.append(source_file_name)
        completed = subprocess.run(compile_commands,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
        if completed.returncode:
            result.append(out_compile)
            out_compile.status = Status.COMPILE_ERROR
            out_compile.stdout = completed.stdout.decode('utf-8').rstrip()
            out_compile.stderr = completed.stderr.decode('utf-8').rstrip()


    return out_compile

#creates a new file and dumps the contents given there
#@the name of the new file
def create_file(file_contents, file_name):
    text_file = open(file_name, "w+")
    text_file.write(file_contents)
    text_file.close()
    return file_name
