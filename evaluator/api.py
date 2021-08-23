from flask import Flask, request
from flask_cors import CORS

from examples import problems
from main import Evaluate

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
    res['proDesc'] = problem.GetInformation()['proDesc']
    res['testCases'] = problem.GetExamples()
    return res

@app.route('/judge', methods=['POST'])
def judge():
    target = request.json
    problemId = target['proNum']
    source = target['code']

    problem = problems[problemId]

    resType, failReason = Evaluate(source, problem)
    success = resType == 0

    res = dict()
    res['result'] = success
    res['resultDesc'] = resType

    return res

if __name__ == '__main__':
    app.run()