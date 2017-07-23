import requests
import requests.exceptions

from tieronepointfive.enums import State, Transition
from tieronepointfive.evaluation_helpers.transitions import get_best_transition, TransitionRule


class HttpHelper:
    def __init__(self, config):
        self._config = config

    def evaluate(self, tick):
        sites = [
            'https://www.google.com',
            'https://www.bing.com',
        ]
        sites_reached = 0
        for site in sites:
            try:
                req = requests.get(site, timeout=10)
            except requests.exceptions.RequestException:
                pass
            else:
                if req.status_code == 200:
                    sites_reached += 1

        if sites_reached == len(sites):
            transition = Transition.ALL_SITES_REACHED
        elif sites_reached == 0:
            transition = Transition.NO_SITES_REACHED
        else:
            transition = Transition.SOME_SITES_REACHED

        if transition == Transition.ALL_SITES_REACHED:
            end_state, is_terminal = self._get_success_end_state(tick.start_state)
        else:
            end_state, is_terminal = self._get_failure_end_state(tick.start_state)

        tick.complete(transition, end_state, is_terminal)

        return tick

    @staticmethod
    def _get_success_end_state(start_state):
        return State.CONNECTION_WORKING, True

    def _get_failure_end_state(self, start_state):
        rules = [
            TransitionRule(
                State.CONNECTION_WORKING,
                State.CONNECTION_FAILED,
                True,
                lambda config: True
            ),
            TransitionRule(
                State.CONNECTION_FAILED,
                State.CABLE_MODEM_REBOOT_NEEDED,
                False,
                lambda config: config.can_reboot_cable_modem
            ),
            TransitionRule(
                State.CABLE_MODEM_REBOOTING,
                State.ROUTER_REBOOT_NEEDED,
                False,
                lambda config: False
            ),
            TransitionRule(
                State.CABLE_MODEM_REBOOT_FAILED,
                State.ROUTER_REBOOT_NEEDED,
                False,
                lambda config: False
            ),
        ]

        return get_best_transition(rules, self._config, start_state)
