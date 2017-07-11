import pytest

from tieronepointfive.enums import State
from tieronepointfive.evaluator import Evaluator, MissingEvaluatorError
from tieronepointfive.state_machine import StateMachineTick


def test_missing_evaluator_helper():
    empty_evaluator = Evaluator(None)
    starting_tick = StateMachineTick(State.CONNECTION_FAILED)
    with pytest.raises(MissingEvaluatorError):
        empty_evaluator.evaluate(starting_tick)
