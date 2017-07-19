import datetime

from tieronepointfive.evaluator_factory import create_evaluator
from tieronepointfive.state_machine import StateMachine


class Controller:
    def __init__(self, print_to_stdout=True):
        self._print_to_stdout = print_to_stdout

        evaluator = create_evaluator()
        self._state_machine = StateMachine(evaluator, None)
        self._last_run_tick = None

    def _print(self, msg):
        if self._print_to_stdout:
            print('[{0}]: {1}'.format(datetime.datetime.now(), msg))

    def run(self):
        self._print('Starting Tier 1.5')
        self._print('Last tick from last run: {0}'.format(self._last_run_tick))

        is_terminal = False
        while not is_terminal:
            tick_list = self._state_machine.evaluate()
            new_tick = tick_list[-1]
            self._print(new_tick)
            is_terminal = self._state_machine.is_terminal_state()
