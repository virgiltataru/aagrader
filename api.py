from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from requests import put, get
from Classes import Status
from runner import run_source
from test_data import tc1, python3_source_code_add_two_numbers, tc2
import flask
import json
from Classes import Testcase
from model import *
from database import db_session
from model import User



app= Flask(__name__)
api= Api(app)

class check_code(Resource):
    def get(self):
        return {'about':'Hi! Do you want me to check your code?'}

    def post(self):
        # if input from JSON
        json_data = request.get_json(force=True)
        python3_code= json_data['submitted_code']
        test_input= json_data['test_input']
        test_output= json_data['test_output']
        extension= json_data['extension']


        tc1 = Testcase()
        tc1.id = "1"
        tc1.input = test_input
        tc1.timeout = 1

        out = run_source(python3_code, extension , None, ["python3", "Source.py"], [tc1])

        print(out)
        try:
            assert 1 != len(out)
            return {'message':'Something got wrong', 'result': str(out), 'pass':-1}, 201
        except:
            pass
        try:
            assert str(test_output) == out[0].stdout
            assert Status.OK == out[0].status
            return {'result':str(out), 'remarks': 'Code submitted is correct!', 'pass':1}, 201
        except:
            return {'result':str(out), 'remarks': 'Code submitted is incorrect', 'pass':0}, 201



api.add_resource(check_code,'/')

if __name__=='__main__':
    app.run(debug=True)
