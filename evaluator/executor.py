import subprocess
import os
import random


def Execute(command, fin, reqId):
    """
    Execute(command : list[string], fin : File, reqId : str) : tuple(success: boolean, output: string, error: string)
    
    executes given command with subprocess module.
    """
    
    id = random.randrange(1, 100000)
    id = str(id)


    fout = open(reqId+'out'+id+'.txt', 'w')
    ferr = open(reqId+'err'+id+'.txt', 'w')

    subprocess.run(command, stdin = fin, stdout = fout, stderr = ferr)

    fout.close()
    ferr.close()


    fout = open(reqId+'out'+id+'.txt', 'r')
    ferr = open(reqId+'err'+id+'.txt', 'r')

    output = fout.read()
    error = ferr.read()

    fout.close()
    ferr.close()

    os.remove(reqId+'out'+id+'.txt')
    os.remove(reqId+'err'+id+'.txt')


    if len(error) > 0:
        return False, output, error

    return True, output, error