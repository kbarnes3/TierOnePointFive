from tieronepointfive.enums import State, Transition
from tieronepointfive.state_machine import StateMachine, StateMachineTick

from .mock_evaluator import MockEvaluator

def test_basic_tick():
    mock_evaluator = MockEvaluator()

    start_tick = StateMachineTick(State.CONNECTION_WORKING)
    machine = StateMachine(mock_evaluator, start_tick)
    end_tick = machine.evaluate()

    assert end_tick.is_complete()
    assert end_tick.start_state == State.CONNECTION_WORKING
    assert end_tick.end_state == State.CONNECTION_WORKING
    assert end_tick.transition == Transition.ALL_SITES_REACHED

