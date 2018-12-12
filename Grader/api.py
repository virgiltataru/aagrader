from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from requests import put, get
from Classes import *
from runner import run_source
from test_data import *
import flask
import json
from testcase_from_file import *
from flask import Flask
from flask_pymongo import PyMongo
from Grader import *
import importlib
from check_similarity import *


app = Flask(__name__)
# Connect to the mongo db database running at the local server.
app.config["MONGO_URI"] = "mongodb://localhost:27017/autograder"
mongo = PyMongo(app)


app= Flask(__name__)

# just to test
@app.route('/', methods=['GET'])
def get():
    return jsonify({'test':"OK"})
# just to test
@app.route('/', methods=['POST'])
def post():
    json_data = request.get_json(force=True)
    test= json_data['test']
    return jsonify({'test':str(test)})

# get all submission of a student.
@app.route('/get_by_name/<name>', methods=['GET'])
def get_by_name(name):
    ans= mongo.db.submissions.find({"Student": name})
    documents={}
    pas=[]
    fail=[]
    i=0
    for document in ans:
        documents["document "+str(i)]= str(document)
        i=i+1
        if document['result']== 'pass':
            pas.append(document['assignment_id'])
        else:
            fail.append(document['assignment_id'])
    documents["report"]={"pass": pas, "total_pass": len(pas), "fail": fail, "total_fail":len(fail)}
    return jsonify(documents)

# get all submission of a class.
@app.route('/get_by_class_name/<name>', methods=['GET'])
def get_by_class_name(name):
    ans= mongo.db.submissions.find({"class": name})
    documents={}
    assignments={}

    i=0
    for document in ans:
        documents["document "+str(i)]= str(document)
        i=i+1
        if document['assignment_id'] not in assignments.keys():
            assignments[document['assignment_id']]={ "pass":[],"total_pass":0, "fail":[], "total_fail":0 }

        if document['result']== 'pass':
            assignments[document['assignment_id']]["pass"].append(document['Student'])
            assignments[document['assignment_id']]["total_pass"]=assignments[document['assignment_id']]["total_pass"]+1
        else:
            assignments[document['assignment_id']]["fail"].append(document['Student'])
            assignments[document['assignment_id']]["total_fail"]=assignments[document['assignment_id']]["total_fail"]+1
    documents["report_by_assignment"]=assignments
    return jsonify(documents)

# get all similar submissions using assignment id
@app.route('/check_submissions_similarity/<id>', methods=['GET'])
def get_submission_similarity(id):
    ans = check_similarity(mongo, id)
    return jsonify(ans)

# for an assignment, get all submission of all the students.
@app.route('/get_by_assignment_id/<id>', methods=['GET'])
def get_by_assignment_id(id):
    ans= mongo.db.submissions.find({"assignment_id": int(id)})
    documents={}
    pas=[]
    fail=[]
    i=0
    for document in ans:
        documents["document "+str(i)]= str(document)
        i=i+1
        if document['result']== 'pass':
            pas.append(document['Student'])
        else:
            fail.append(document['Student'])
    documents["report"]={"pass": pas, "total_pass": len(pas), "fail": fail, "total_fail":len(fail)}
    return jsonify(documents)

#check code and return a report.
@app.route('/check_code', methods=['POST'])
def check_code():
    # if input from JSON
    json_data = request.get_json(force=True)
    # if code variable is empty read from the file
    code= json_data['code']
    if code=="":
        code_file= json_data['code_file']
        # read the file
        f= open("code/"+code_file+".txt",'r')
        file= f.read()

        # update the code variable
        code= file

    # if test cases are also in the file
    test_input= json_data['test_input']
    test_cases=[]
    if test_input !=[]:
        # make all the test cases
        test_output= json_data['test_output']
        for i in range(len(test_input)):
            test_cases.append(Testcase())
            test_cases[i].id= str(i)
            test_cases[i].input= test_input[i]
            test_cases[i].expected_output= test_output[i]
            #return jsonify({'test':test_cases[0].input, "out": str(test_cases[0].expected_output)})
    else:
        test_input_files= json_data['test_input_files']
        for i in range(len(test_input_files)):
            test_cases.append(get_test_case("test_case/"+test_input_files[i]+".txt"))
            # return jsonify({'test':test_cases[0].input, "out": str(test_cases[0].expected_output)})



    # other inouts from postman
    extension= json_data['extension']
    student= json_data['student']
    assignment_id= json_data['assignment_id']
    pass_req= json_data['pass_req']
    max_lines= json_data['max_lines']
    clas= json_data['class']
    code_total_lines= len(code.split('\n'))
    if code_total_lines> max_lines:
        return jsonify({'Message':"Error: # lines of code are more than permitted.", "code_total_lines": code_total_lines})


    # make a submission object
    sub= Submission()
    sub.source= code
    sub.file_extension= extension
    sub.student= student


    # test the code
    result= grade(sub, test_cases )
    #add add assignment ID to the result file
    result['code_total_lines']= code_total_lines
    result['assignment_id']= assignment_id
    result['pass_req']= pass_req
    result['class']= clas

    if result['tests_passed']>=result['pass_req']:
        result['result']="pass"
    else:
        result['result']="fail"
    # add result to the the database
    mongo.db.submissions.insert_one(result)

    return jsonify({'Output':str(result)})



if __name__=='__main__':
    app.run(debug=True)
