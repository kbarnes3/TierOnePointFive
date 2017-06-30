from tieronepointfive.enums import State, Transition


class MockEvaluator:
    def __init__(self, evaluation_func):
        self.evaluation_func = evaluation_func

    def evaluate_tick(self, tick):
        transition, end_state = self.evaluation_func()
        tick.complete(transition, end_state)
        return tick
