from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from requests import put, get

app= Flask(__name__)
api= Api(app)

class check_code(Resource):
    def get(self):
        # Use if required
        return {'about':'hello_world'}

    def post(self):
        # { problem_id: __ , 'test_case': ___ , 'submitted_code': ___ }
        json_data = request.get_json(force=True)

        # each problem has a problem ID. This might be useful. Discard if not required
        problem_id = json_data['problem_id']

        # 'test_case': {'id':___ , 'input':____ , 'file'____ }
        test_case = json_data['test_case']

        # 'submitted_code': {'source':__, 'programming_language': 'python'}
        code_submitted= json_data['submitted_code']

        # Call all the classes to check the code_sibmitted




        # to send the output back to the other webservice.
            # put('http://localhost:5000/', data={'data': 'this is the data'}).json()
        put('', data={'data': 'Congratulations! this is done.'}).json()

        # return function might also do the job
        return {'you_sent':some_json}, 201


api.add_resource(check_code,'/')

if __name__=='__main__':
    app.run(debug=True)
