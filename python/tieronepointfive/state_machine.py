class StateMachineTick:
    def __init__(self, state):
        self.start_state = state
        self.transition = None
        self.end_state = None

    def complete(self, transition, end_state):
        if self.is_complete():
            raise "Unable to complete a completed tick"
        self.transition = transition
        self.end_state = end_state
    
    def is_complete(self):
        return (self.transition is not None) and (self.end_state is not None)


class StateMachine:
    def __init__(self, evaluator, tick):
        self.evaluator = evaluator
        self.tick = tick

    def evaluate(self):
        if self.tick.is_complete():
            raise "Unable to evaluate a completed tick"
        completed_tick = self.evaluator.evaluate_tick(self.tick)
        self.tick = StateMachineTick(completed_tick.end_state)
        return completed_tick
