from .enums import State


class MissingEvaluatorError(Exception):
    def __init__(self, tick):
        super().__init__("Missing helper for tick in state {0}".format(tick.start_state))


class MissingHelper:
    def evaluate(self, tick):
        raise MissingEvaluatorError(tick)


class Evaluator:
    def __init__(self):
        self._evaluator_helpers = {}

    def evaluate(self, tick):
        if tick.is_complete():
            raise Exception("Can't evaluate an already completed tick")

        evaluator = self._evaluator_helpers.get(tick.start_state, MissingHelper())

        completed_tick = evaluator.evaluate(tick)
        return completed_tick
