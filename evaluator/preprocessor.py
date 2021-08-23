import os

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