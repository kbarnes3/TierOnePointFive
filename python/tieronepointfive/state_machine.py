class StateMachineTick:
    def __init__(self, start_state, transition=None, end_state=None):
        self.start_state = start_state
        self.transition = transition
        self.end_state = end_state

    def complete(self, transition, end_state):
        if self.is_complete():
            raise Exception("Unable to complete a completed tick")
        self.transition = transition
        self.end_state = end_state
    
    def is_complete(self):
        return (self.transition is not None) and (self.end_state is not None)


class StateMachine:
    def __init__(self, evaluator, tick_list):
        self.evaluator = evaluator
        self.tick_list = tick_list

    def evaluate(self):
        last_tick = self.tick_list[-1]
        new_tick = StateMachineTick(last_tick.end_state)
        completed_tick = self.evaluator.evaluate_tick(new_tick)
        self.tick_list.append(completed_tick)
        return self.tick_list
