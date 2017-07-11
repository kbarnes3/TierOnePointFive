from tieronepointfive.enums import State, Transition


class HttpHelper:
    def evaluate(self, tick):
        tick.complete(Transition.NO_SITES_REACHED, State.CONNECTION_FAILED, True)
