from preprocessor import PreprocessPython, PreprocessCPP, PreprocessC, PreprocessJava
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
-4: timelimit exceeded
-5: memory exceeded
"""

def Evaluate(code, language, problem):
    """
    Evaluate(code : string, problem : Problem) : tuple(resultType : int, failReason : string)
    """
    reqId = random.randrange(1, 100000)
    reqId = str(reqId)

    PreprocessSelector = None

    if language == 1:
        # python
        PreprocessSelector = PreprocessPython
    elif language == 2:
        # c++
        PreprocessSelector = PreprocessCPP
    elif language == 3:
        # c
        PreprocessSelector = PreprocessC
    elif language == 4:
        # java
        PreprocessSelector = PreprocessJava

    preprocessSucceed, executeCommand, clear, preprocessError = PreprocessSelector(code, reqId)
    if not preprocessSucceed:
        try:
            clear()
        except:
            pass
        return 1, preprocessError
    
    for case in problem.GetCases():
        fin = open(reqId + 'input.txt', 'w')
        fin.write(case.GetInputData())
        fin.close()

        fin = open(reqId + 'input.txt', 'r')
        executeSucceed, executeResult, executeError = Execute(executeCommand, fin, problem.GetTimeLimit())
        fin.close()

        os.remove(reqId + 'input.txt')

        if executeSucceed == 1:
            print(executeError)
            clear()
            return 2, executeError
        
        if executeSucceed == 2:
            clear()
            return 4, executeError
            
        if not Assess(executeResult, case.GetCriteria()):
            clear()
            return 3, 'Wrong Answer'

    clear()
    return 0, ''