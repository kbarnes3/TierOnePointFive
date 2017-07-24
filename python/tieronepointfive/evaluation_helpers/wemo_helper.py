from collections import namedtuple
from time import sleep

from ouimeaux.environment import Environment

from tieronepointfive.enums import State, Transition


class WemoHelper:
    def __init__(self, config):
        self._config = config

    def evaluate(self, tick, **kwargs):
        WemoMode = namedtuple('WemoMode', ['switch_name', 'success_transition', 'success_end_state', 'failure_transition', 'failure_end_state'])
        modes = {
            State.CABLE_MODEM_REBOOT_NEEDED:
                WemoMode(
                    self._config.cable_modem_switch,
                    Transition.CABLE_MODEM_POWER_CYCLED,
                    State.CABLE_MODEM_REBOOTING,
                    Transition.CABLE_MODEM_POWER_CYCLE_FAILED,
                    State.CABLE_MODEM_REBOOT_FAILED
                ),
            State.ROUTER_REBOOT_NEEDED:
                WemoMode(
                    self._config.router_switch,
                    Transition.ROUTER_POWER_CYCLED,
                    State.ROUTER_REBOOTING,
                    Transition.ROUTER_POWER_CYCLE_FAILED,
                    State.ROUTER_REBOOT_FAILED
                )
        }

        mode = modes[tick.start_state]
        switch_name = mode.switch_name
        try:
            self._toggle_switch(switch_name)
        except:
            transition = mode.failure_transition
            end_state = mode.failure_end_state
        else:
            transition = mode.success_transition
            end_state = mode.success_end_state

        tick.complete(transition, end_state, True)

        return tick

    @staticmethod
    def _toggle_switch(switch_name):
        env = Environment()
        env.start()
        env.discover(seconds=2)

        switch = env.get_switch(switch_name)
        switch.off()
        sleep(10)
        switch.on()
