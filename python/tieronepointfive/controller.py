from tieronepointfive.evaluator_factory import create_evaluator
from tieronepointfive.state_machine import StateMachine


class Controller:
    def __init__(self):
        evaluator = create_evaluator()
        self._state_machine = StateMachine(evaluator, None)
