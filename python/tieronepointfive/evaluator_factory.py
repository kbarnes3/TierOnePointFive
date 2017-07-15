from tieronepointfive.evaluator import Evaluator
from tieronepointfive.evaluation_helpers import HttpHelper


def create_evaluator():
    http_helper = HttpHelper()
    evaluator = Evaluator(http_helper)

    return evaluator