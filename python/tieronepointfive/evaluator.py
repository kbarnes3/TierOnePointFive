from .enums import State


class Evaluator:
    def __init__(self, http_helper):
        self._evaluator_helpers = {
            State.CONNECTION_WORKING: http_helper
        }

    def evaluate(self, tick):
        if tick.is_complete():
            raise Exception("Can't evaluate an already completed tick")

        evaluator = self._evaluator_helpers[tick.is_complete]

        completed_tick = evaluator.evaluate(tick)
        return completed_tick
