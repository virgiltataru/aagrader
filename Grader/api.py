from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from requests import put, get
from Classes import *
from runner import run
from test_data import *
import flask
import json
from testcase_from_file import *
from flask import Flask
from flask_pymongo import PyMongo
from Grader import *
import importlib



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/autograder"
mongo = PyMongo(app)


app= Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return jsonify({'test':"OK"})

@app.route('/', methods=['POST'])
def post():
    json_data = request.get_json(force=True)
    test= json_data['test']
    return jsonify({'test':str(test)})

@app.route('/get_by_name/<name>', methods=['GET'])
def get_by_name(name):
    ans= mongo.db.submissions.find({"Student": name})
    documents={}
    i=0
    for document in ans:
        documents["document "+str(i)]= str(document)
        i=i+1
    return jsonify(documents)

@app.route('/get_by_assignment_id/<id>', methods=['GET'])
def get_by_assignment_id(id):
    ans= mongo.db.submissions.find({"assignment_id": id})
    documents={}
    i=0
    for document in ans:
        documents["document "+str(i)]= str(document)
        i=i+1
    return jsonify(documents)


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
            return jsonify({'test':test_cases[0].input, "out": str(test_cases[0].expected_output)})
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

    # make a submission object
    sub= Submission()
    sub.source= code
    sub.file_extension= extension
    sub.student= student


    # test the code
    result= grade(sub, test_cases )
    #add add assignment ID to the result file
    code_total_lines= len(code.split('\n'))
    result['code_total_lines']= code_total_lines
    result['assignment_id']= assignment_id
    result['pass_req']= pass_req


    if result['tests_passed']>=result['pass_req']:
        result['result']="pass"
    else:
        result['result']="fail"
    # add result to the the database
    mongo.db.submissions.insert_one(result)

    return jsonify({'Output':str(result)})
    return result



if __name__=='__main__':
    app.run(debug=True)