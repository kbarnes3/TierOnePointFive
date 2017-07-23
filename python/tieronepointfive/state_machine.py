from .enums import State


class StateMachineTick:
    def __init__(self, start_state):
        self.start_state = start_state
        self.transition = None
        self.end_state = None
        self.is_terminal = None

    def __repr__(self):
        return '<StateMachineTick start_state:{0} transition:{1} end_state:{2} is_terminal:{3}>'.format(
            repr(self.start_state),
            repr(self.transition),
            repr(self.end_state),
            repr(self.is_terminal)
        )

    def __str__(self):
        return 'Tick: "{0}" => "{1}" => "{2}" Terminal: {3}'.format(
            str(self.start_state),
            str(self.transition),
            str(self.end_state),
            str(self.is_terminal)
        )

    @classmethod
    def create_completed(cls, start_state, transition, end_state, is_terminal):
        tick = cls(start_state)
        tick.complete(transition, end_state, is_terminal)
        return tick

    def complete(self, transition, end_state, is_terminal):
        if self.is_complete():
            raise Exception("Unable to complete a completed tick")
        self.transition = transition
        self.end_state = end_state
        self.is_terminal = is_terminal
    
    def is_complete(self):
        return (self.transition is not None) and (self.end_state is not None)

    def is_steady(self):
        return self.end_state == State.CONNECTION_WORKING


class StateMachine:
    def __init__(self, evaluator, tick_list):
        self.evaluator = evaluator
        self.tick_list = tick_list

    def evaluate(self):
        last_tick = self.tick_list[-1]
        new_tick = StateMachineTick(last_tick.end_state)

        completed_tick = self.evaluator.evaluate_tick(new_tick)
        if completed_tick.is_steady():
            self.tick_list = [completed_tick]
        else:
            self.tick_list.append(completed_tick)
        return self.tick_list

    def is_terminal_state(self):
        return self.tick_list[-1].is_terminal
