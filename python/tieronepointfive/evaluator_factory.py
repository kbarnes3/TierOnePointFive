from tieronepointfive.evaluator import Evaluator
from tieronepointfive.evaluation_helpers import HttpHelper, WemoHelper


def create_evaluator(config):
    http_helper = HttpHelper(config)
    wemo_helper = WemoHelper(config)
    evaluator = Evaluator(http_helper, wemo_helper)

    return evaluator
