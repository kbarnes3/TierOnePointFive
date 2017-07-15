from tieronepointfive.evaluator_factory import create_evaluator
from tieronepointfive.state_machine import StateMachine


class Controller:
    def __init__(self, print_to_stdout = True):
        self._print_to_stdout = print_to_stdout

        evaluator = create_evaluator()
        self._state_machine = StateMachine(evaluator, None)

    def _print(self, msg):
        if self._print_to_stdout:
            print(msg)
