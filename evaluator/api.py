from flask import Flask, request
from flask_cors import CORS

from examples import problems
from main import Evaluate

import requests
import json

import sys

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/problems')
def get_problems():
    problemsSummary = []
    for key in problems:
        info = problems[key].GetInformation()
        del info['proDesc']
        problemsSummary.append(info)

    res = dict()
    res['problems'] = problemsSummary
    return res

@app.route('/problem/<problem_id>')
def get_problem_by_id(problem_id):
    problem = problems[int(problem_id)]

    res = dict()
    proLabels = problem.GetInformation()
    res['proTitle'] = proLabels['proTitle']
    res['proDesc'] = proLabels['proDesc']
    res['testCases'] = problem.GetExamples()
    return res

@app.route('/judge', methods=['POST'])
def judge():
    target = request.json
    problemId = target['proNum']
    source = target['code']
    language = target['langtype']

    problem = problems[problemId]

    if language == 4:
        headers = {
            'Content-Type': 'application/json;'
        }

        data = {
            'proNum': problemId,
            'code': source,
            'langtype': language
        }

        print('aaa', sys.stderr)
        print(json.dumps(data), sys.stderr)
        res = requests.post('http://judge-java:5000/judge', data = json.dumps(data), headers = headers)
        print(res.text, sys.stderr)
        print(res.json(), sys.stderr)
        return  res.json()

    resType, failReason = Evaluate(source, language, problem)
    success = resType == 0

    res = dict()
    res['result'] = success
    res['resultDesc'] = resType

    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0')