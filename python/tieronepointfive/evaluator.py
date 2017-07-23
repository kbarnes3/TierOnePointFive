from .enums import State


class Evaluator:
    def __init__(self, http_helper):
        self._evaluator_helpers = {
            State.FRESH_DATA_FILE: http_helper,
            State.CONNECTION_WORKING: http_helper
        }

    def evaluate_tick(self, tick):
        if tick.is_complete():
            raise Exception("Can't evaluate an already completed tick")

        evaluator = self._evaluator_helpers[tick.start_state]

        completed_tick = evaluator.evaluate(tick)
        return completed_tick
