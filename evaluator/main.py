from preprocessor import PreprocessPython
from executor import Execute


def Eveluate():
    preprocessSucceed, executeCommand, preprocessError = PreprocessPython(code)
    if not preprocessSucceed:
        return preprocessError
    
    executeSucceed, executeError = Execute(executeCommand)
    if not executeSucceed:
        return executeError