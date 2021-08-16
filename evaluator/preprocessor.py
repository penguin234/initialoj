

def PreprocessPython(code):
    """
    PreprocessPython(code : string) : tuple(success: boolean, command: list[string], error: string)
    
    Preprocesses python file of given code
    """
    codeFileName = "source.py"

    codeFile = open(codeFileName, "w")
    codeFile.write(code)
    codeFile.close()

    return True, ["python", codeFileName], ""