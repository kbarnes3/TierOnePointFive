import requests
import requests.exceptions

from tieronepointfive.enums import State, Transition


class HttpHelper:
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
            end_state = State.CONNECTION_WORKING
        else:
            end_state = State.CONNECTION_FAILED

        tick.complete(transition, end_state, True)

        return tick
