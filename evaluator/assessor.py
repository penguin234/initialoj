

class SimpleCriteria:
    def __init__(self, answer):
        self._answerSheet = answer.strip()

    def Assess(self, target):
        return target.strip() == self._answerSheet
        


def Assess(output, criteria):
    return criteria.Assess(output)