from .enums import State


class MissingHelper:
    def evaluate(self, tick):
        raise Exception("Missing helper for tick in state {0}".format(tick.start_state))


class Evaluator:
    def __init__(self):
        self._evaluator_helpers = {}

    def evaluate(self, tick):
        if tick.is_complete():
            raise Exception("Can't evaluate an already completed tick")

