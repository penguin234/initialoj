from assessor import SimpleCriteria

from copy import deepcopy


class Case:
    def __init__(self, input, answer):
        self._inputdata = input
        self._criteria = SimpleCriteria(answer)
    
    def GetInputData(self):
        return self._inputdata

    def GetCriteria(self):
        return self._criteria


class Problem:
    def __init__(self, inputs, answers, title, id, desc, examples, timeLimit):
        self._cases = []
        for input, answer in zip(inputs, answers):
            self._cases.append(Case(input, answer))
        
        self._title = title
        self._id = id
        self._desc = desc
        self._timeLimit = timeLimit
        self._examples = deepcopy(examples)
    
    def GetCases(self):
        return deepcopy(self._cases)

    def GetTimeLimit(self):
        return self._timeLimit

    def GetInformation(self):
        res = dict()
        res['proTitle'] = self._title
        res['proNum'] = self._id
        res['proDesc'] = self._desc
        res['proTimeLimit'] = self._timeLimit
        return res
    
    def GetExamples(self):
        res = []
        for example in self._examples:
            res.append({
                'inputEx': example[0],
                'outputEx': example[1],
            })
        return res