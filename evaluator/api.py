from flask import Flask
from flask_cors import CORS

from examples import problems

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


if __name__ == '__main__':
    app.run()