from tieronepointfive.evaluator import Evaluator
from tieronepointfive.evaluation_helpers import HttpHelper


def create_evaluator(config):
    http_helper = HttpHelper(config)
    evaluator = Evaluator(http_helper)

    return evaluator
