from tieronepointfive.enums import State, Transition


class MockEvaluator:
    def __init__(self, evaluation_generator):
        self.evaluation_generator = evaluation_generator

    def evaluate_tick(self, tick):
        transition, end_state = next(self.evaluation_generator)
        tick.complete(transition, end_state)
        return tick
