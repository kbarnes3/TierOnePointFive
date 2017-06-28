from tieronepointfive.enums import State, Transition
from tieronepointfive.state_machine import StateMachine, StateMachineTick

from .mock_evaluator import MockEvaluator


def _assert_ticks_equal(actual_tick, expected_tick):
    assert actual_tick.is_complete() == expected_tick.is_complete()
    assert actual_tick.start_state == expected_tick.start_state
    assert actual_tick.transition == expected_tick.transition
    assert actual_tick.end_state == expected_tick.end_state


def test_non_steady_ticks():
    def verify_tick_list(tick_list, expected_length):
        assert len(tick_list) == expected_length

        start_tick = tick_list[0]
        expected_start_tick = StateMachineTick(State.CONNECTION_WORKING, Transition.ALL_SITES_REACHED, State.CONNECTION_WORKING)
        _assert_ticks_equal(start_tick, expected_start_tick)

        second_tick = tick_list[1]
        expected_second_tick = StateMachineTick(State.CONNECTION_WORKING, Transition.NO_SITES_REACHED, State.CONNECTION_FAILED)
        _assert_ticks_equal(second_tick, expected_second_tick)

        expected_other_tick = StateMachineTick(State.CONNECTION_FAILED, Transition.NO_SITES_REACHED, State.CONNECTION_FAILED)
        for i in range(2, len(tick_list)):
            _assert_ticks_equal(tick_list[i], expected_other_tick)

    mock_evaluator = MockEvaluator()

    start_tick = StateMachineTick(State.CONNECTION_WORKING, Transition.ALL_SITES_REACHED, State.CONNECTION_WORKING)
    machine = StateMachine(mock_evaluator, [start_tick])

    for i in range(2, 15):
        tick_list = machine.evaluate()
        verify_tick_list(tick_list, i)


