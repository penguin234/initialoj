import subprocess

inputFileName = "input.txt"
outputFileName = "output.txt"
errorFileName = "error.txt"

def Execute(command):
    """
    Execute(command : list[string]) : tuple(success: boolean, error: string)
    
    executes given command with subprocess module.
    """
    inputFile = open(inputFileName, "r")
    outputFile = open(outputFileName, "w")
    errorFile = open(errorFileName, "w")

    subprocess.run(command, stdin = inputFile, stdout = outputFile, stderr = errorFile)

    inputFile.close()
    outputFile.close()
    errorFile.close()

    return True, ""