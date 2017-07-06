class MockEvaluator:
    def __init__(self, evaluation_generator):
        self.evaluation_generator = evaluation_generator

    def evaluate_tick(self, tick):
        transition, end_state, is_terminal = next(self.evaluation_generator)
        tick.complete(transition, end_state, is_terminal)
        return tick
