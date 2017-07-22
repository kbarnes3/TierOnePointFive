import argparse
import sys

from tieronepointfive.config import Config
from tieronepointfive.controller import Controller


def run():
    _process_command_line(sys.argv[1:])


def _process_command_line(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_dir')
    args = parser.parse_args(argv)

    config = Config(args.config_dir)
    controller = Controller()
    controller.run()
