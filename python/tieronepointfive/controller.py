import datetime

from tieronepointfive.data import DataPickler
from tieronepointfive.evaluator_factory import create_evaluator
from tieronepointfive.state_machine import StateMachine


class Controller:
    def __init__(self, config, print_to_stdout=True):
        self._config = config
        self._print_to_stdout = print_to_stdout

        evaluator = create_evaluator(config)
        self._pickler = DataPickler(config)

        self._data = self._pickler.load()
        self._state_machine = StateMachine(evaluator, self._data.tick_list)

    def _print(self, msg):
        if self._print_to_stdout:
            print('[{0}]: {1}'.format(datetime.datetime.now(), msg))

    def _print_tick(self, tick):
        if self._print_to_stdout:
            print(tick)

    def run(self):
        self._print('Starting Tier 1.5')
        self._print('Data directory: {0}'.format(self._config.data_directory))
        self._print('Loading {0} ticks'.format(len(self._data.tick_list)))
        self._print('Last tick from last run: {0}'.format(self._data.tick_list[-1]))

        is_terminal = False
        while not is_terminal:
            tick_list = self._state_machine.evaluate()
            new_tick = tick_list[-1]
            self._print_tick(new_tick)
            is_terminal = self._state_machine.is_terminal_state()

        self._data.tick_list = tick_list
        self._pickler.dump(self._data)
