class StateMachineTick:
    def __init__(self):
        self.start_state = 0
        self.end_state = None
    
    def is_complete(self):
        return self.end_state is not None


class StateMachine:
    def __init__(self, tick):
        self.tick = tick

    def evaluate(self):
        if self.tick.is_complete():
            raise "Unable to evaluate a completed tick"
