from tieronepointfive.evaluator import Evaluator
from tieronepointfive.evaluation_helpers import EmailHelper, HttpHelper, WemoHelper


def create_evaluator(config):
    email_helper = EmailHelper(config)
    http_helper = HttpHelper(config)
    wemo_helper = WemoHelper(config)
    evaluator = Evaluator(email_helper, http_helper, wemo_helper)

    return evaluator
