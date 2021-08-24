from preprocessor import PreprocessPython
from executor import Execute
from assessor import Assess

import os
import random


"""
resultType
-0: correct
-1: compile error
-2: runtime error
-3: wrong answer
"""

def Evaluate(code, problem):
    """
    Evaluate(code : string, problem : Problem) : tuple(resultType : int, failReason : string)
    """
    reqId = random.randrange(1, 100000)
    reqId = str(reqId)

    preprocessSucceed, executeCommand, clear, preprocessError = PreprocessPython(code, reqId)
    if not preprocessSucceed:
        return 1, preprocessError
    
    for case in problem.GetCases():
        fin = open(reqId + 'input.txt', 'w')
        fin.write(case.GetInputData())
        fin.close()

        fin = open(reqId + 'input.txt', 'r')
        executeSucceed, executeResult, executeError = Execute(executeCommand, fin, reqId)
        fin.close()

        os.remove(reqId + 'input.txt')

        if not executeSucceed:
            clear()
            return 2, executeError
        
        if not Assess(executeResult, case.GetCriteria()):
            clear()
            return 3, 'Wrong Answer'

    clear()
    return 0, ''