import sys

from tieronepointfive.controller import Controller


def run():
    _process_command_line(sys.argv)


def _process_command_line(argv):
    controller = Controller()
    controller.run()
