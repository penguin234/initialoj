import subprocess
from threading import Timer
import time
import sys


def Execute(command, fin, timeLimit):
    """
    Execute(command : list[string], fin : File, reqId : str) : tuple(result: int, output: string, error: string)
    
    -result
        0: success
        1: runtime error
        2: timeout
    
    executes given command with subprocess module.
    """

    p = subprocess.Popen(command, stdin = fin, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
    timer = Timer(timeLimit * 2 / 1000.0, p.kill)

    timer.start()

    startTime = time.time()
    output, error = p.communicate()
    endTime = time.time()

    #print(str(endTime - startTime), file = sys.stderr)

    if timer.is_alive():
        timer.cancel()
    else:
        return 2, output, str(endTime - startTime)

    
    if endTime - startTime > timeLimit / 1000.0:
        return 2, output, str(endTime - startTime)

    if len(error) > 0:
        return 1, output, error


    return 0, output, error