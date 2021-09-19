import os
import shutil
import subprocess

def PreprocessPython(code, reqId):
    """
    PreprocessPython(code : string, reqId : string) : tuple(success: boolean, command: list[string], clear: func, error: string)
    
    Preprocesses python file of given code
    """
    codeFileName = reqId + 'source.py'

    codeFile = open(codeFileName, 'w')
    codeFile.write(code)
    codeFile.close()

    def Clear():
        os.remove(codeFileName)

    return True, ['python', codeFileName], Clear, ''

def PreprocessCPP(code, reqId):
    """
    PreprocessCPP(code : string, reqId : string) : tuple(success: boolean, command: list[string], clear: func, error: string)
    
    Preprocesses c++ code and exe file of given code
    """
    codeFileName = reqId + 'source.cpp'
    execFileName = reqId + 'exec'

    codeFile = open(codeFileName, 'w')
    codeFile.write(code)
    codeFile.close()

    errorFileName = reqId + 'err.txt'
    errorFile = open(errorFileName, 'w')

    subprocess.run(['g++', '-o', execFileName, codeFileName], stderr = errorFile)
    errorFile.close()
    
    def Clear():
        os.remove(codeFileName)
        os.remove(execFileName)

    errorFile = open(errorFileName, 'r')
    error = errorFile.read()
    errorFile.close()
    os.remove(errorFileName)

    if len(error) > 0:
        return False, None, Clear, error

    return True, ['./' + execFileName], Clear, ''

def PreprocessC(code, reqId):
    """
    PreprocessC(code : string, reqId : string) : tuple(success: boolean, command: list[string], clear: func, error: string)
    
    Preprocesses c code and exe file of given code
    """
    codeFileName = reqId + 'source.cpp'
    execFileName = reqId + 'exec'

    codeFile = open(codeFileName, 'w')
    codeFile.write(code)
    codeFile.close()

    errorFileName = reqId + 'err.txt'
    errorFile = open(errorFileName, 'w')

    subprocess.run(['gcc', '-o', execFileName, codeFileName], stderr = errorFile)
    errorFile.close()
    
    def Clear():
        os.remove(codeFileName)
        os.remove(execFileName)

    errorFile = open(errorFileName, 'r')
    error = errorFile.read()
    errorFile.close()
    os.remove(errorFileName)

    if len(error) > 0:
        return False, None, Clear, error

    return True, ['./' + execFileName], Clear, ''

def PreprocessJava(code, reqId):
    """
    PreprocessJava(code : string, reqId : string) : tuple(success: boolean, command: list[string], clear: func, error: string)
    
    Preprocesses java code and exe file of given code
    """
    dirName = 'java' + reqId
    os.mkdir(dirName)

    codeFileName = dirName + '/' + 'Main.java'
    execFileName = 'Main'

    codeFile = open(codeFileName, 'w')
    codeFile.write(code)
    codeFile.close()

    errorFileName = dirName + '/' + 'err.txt'
    errorFile = open(errorFileName, 'w')

    subprocess.run(['javac', '-d', dirName, codeFileName], stderr = errorFile)
    errorFile.close()
    
    def Clear():
        shutil.rmtree(dirName)

    errorFile = open(errorFileName, 'r')
    error = errorFile.read()
    errorFile.close()
    os.remove(errorFileName)

    if len(error) > 0:
        return False, None, Clear, error

    return True, ['java', '-cp', dirName, execFileName], Clear, ''
