

class SimpleCriteria:
    def __init__(self, fileName):
        file = open(fileName, 'r')
        self.answerSheet = file.read()
        file.close()

    def Assess(self, target):
        


def Assess(output, criteria):
    