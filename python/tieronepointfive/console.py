import sys

from tieronepointfive.config import Config
from tieronepointfive.controller import Controller


def run():
    _process_command_line(sys.argv)


def _process_command_line(argv):
    config = Config()
    controller = Controller()
    controller.run()
