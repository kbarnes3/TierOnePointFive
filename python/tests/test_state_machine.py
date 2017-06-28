from tieronepointfive.enums import State, Transition
from tieronepointfive.state_machine import StateMachine, StateMachineTick

from .mock_evaluator import MockEvaluator


def test_basic_tick():
    mock_evaluator = MockEvaluator()

    start_tick = StateMachineTick(State.CONNECTION_WORKING, Transition.ALL_SITES_REACHED, State.CONNECTION_WORKING)
    machine = StateMachine(mock_evaluator, [start_tick])
    tick_list = machine.evaluate()
    assert len(tick_list) == 2

    end_tick = tick_list[1]

    assert end_tick.is_complete()
    assert end_tick.start_state == State.CONNECTION_WORKING
    assert end_tick.end_state == State.CONNECTION_FAILED
    assert end_tick.transition == Transition.NO_SITES_REACHED

