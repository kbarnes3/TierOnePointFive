from tieronepointfive.enums import State, Transition


class MockEvaluator:
    def evaluate_tick(self, tick):
        tick.complete(Transition.NO_SITES_REACHED, State.CONNECTION_FAILED)
        return tick
