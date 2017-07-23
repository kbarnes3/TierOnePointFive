from time import sleep

from ouimeaux.environment import Environment

from tieronepointfive.enums import State, Transition


class WemoHelper:
    def __init__(self, config):
        self._config = config

    def evaluate(self, tick):
        env = Environment()
        env.start()
        env.discover(seconds=2)

        switch_name = self._config.cable_modem_switch
        switch = env.get_switch(switch_name)
        switch.off()
        sleep(10)
        switch.on()
