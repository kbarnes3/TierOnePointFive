import itertools

from tieronepointfive.enums import State, Transition
from tieronepointfive.state_machine import StateMachine, StateMachineTick

from .mock_evaluator import MockEvaluator


def _assert_ticks_equal(actual_tick, expected_tick):
    assert actual_tick.is_complete() == expected_tick.is_complete()
    assert actual_tick.is_steady() == expected_tick.is_steady()
    assert actual_tick.start_state == expected_tick.start_state
    assert actual_tick.transition == expected_tick.transition
    assert actual_tick.end_state == expected_tick.end_state
    assert actual_tick.is_terminal == expected_tick.is_terminal


def test_failing_ticks():
    def verify_tick_list(actual_tick_list, expected_length):
        assert len(actual_tick_list) == expected_length

        actual_start_tick = actual_tick_list[0]
        expected_start_tick = StateMachineTick.create_completed(State.CONNECTION_WORKING, Transition.ALL_SITES_REACHED, State.CONNECTION_WORKING, True)
        _assert_ticks_equal(actual_start_tick, expected_start_tick)

        second_tick = actual_tick_list[1]
        expected_second_tick = StateMachineTick.create_completed(State.CONNECTION_WORKING, Transition.NO_SITES_REACHED, State.CONNECTION_FAILED, True)
        _assert_ticks_equal(second_tick, expected_second_tick)

        expected_other_tick = StateMachineTick.create_completed(State.CONNECTION_FAILED, Transition.NO_SITES_REACHED, State.CONNECTION_FAILED, True)
        for i in range(2, len(actual_tick_list)):
            _assert_ticks_equal(actual_tick_list[i], expected_other_tick)

    evaluation_generator = itertools.repeat((Transition.NO_SITES_REACHED, State.CONNECTION_FAILED, True))

    mock_evaluator = MockEvaluator(evaluation_generator)

    start_tick = StateMachineTick.create_completed(State.CONNECTION_WORKING, Transition.ALL_SITES_REACHED, State.CONNECTION_WORKING, True)
    machine = StateMachine(mock_evaluator, [start_tick])

    for i in range(2, 15):
        tick_list = machine.evaluate()
        verify_tick_list(tick_list, i)


def test_steady_state_ticks():
    def verify_tick_list(actual_tick_list):
        assert len(actual_tick_list) == 1

        expected_tick = StateMachineTick.create_completed(State.CONNECTION_WORKING, Transition.ALL_SITES_REACHED, State.CONNECTION_WORKING, True)
        _assert_ticks_equal(actual_tick_list[0], expected_tick)

    evaluation_generator = itertools.repeat((Transition.ALL_SITES_REACHED, State.CONNECTION_WORKING, True))

    mock_evaluator = MockEvaluator(evaluation_generator)

    start_tick = StateMachineTick.create_completed(State.CONNECTION_WORKING, Transition.ALL_SITES_REACHED, State.CONNECTION_WORKING, True)
    machine = StateMachine(mock_evaluator, [start_tick])

    for _ in range(1,15):
        tick_list = machine.evaluate()
        verify_tick_list(tick_list)


def test_typical_ticks():
    def verify_tick_list(actual_tick_list, expected_tick_list):
        assert len(actual_tick_list) == len(expected_tick_list)

        for actual_tick, expected_tick in zip(actual_tick_list, expected_tick_list):
            _assert_ticks_equal(actual_tick, expected_tick)

    expected_ticks = [
        StateMachineTick.create_completed(State.CONNECTION_WORKING, Transition.ALL_SITES_REACHED, State.CONNECTION_WORKING, True),
        StateMachineTick.create_completed(State.CONNECTION_WORKING, Transition.NO_SITES_REACHED, State.CONNECTION_FAILED, True),
        StateMachineTick.create_completed(State.CONNECTION_FAILED, Transition.NO_SITES_REACHED, State.CABLE_MODEM_REBOOT_NEEDED, False),
        StateMachineTick.create_completed(State.CABLE_MODEM_REBOOT_NEEDED, Transition.CABLE_MODEM_POWER_CYCLED, State.CABLE_MODEM_REBOOTING, True),
        StateMachineTick.create_completed(State.CABLE_MODEM_REBOOTING, Transition.NO_SITES_REACHED, State.ROUTER_REBOOT_NEEDED, False),
        StateMachineTick.create_completed(State.ROUTER_REBOOT_NEEDED, Transition.ROUTER_POWER_CYCLED, State.ROUTER_REBOOTING, True),
        StateMachineTick.create_completed(State.ROUTER_REBOOTING, Transition.ALL_SITES_REACHED, State.EMAIL_QUEUED, False),
        StateMachineTick.create_completed(State.EMAIL_QUEUED, Transition.EMAIL_SENT, State.CONNECTION_WORKING, True),
        StateMachineTick.create_completed(State.CONNECTION_WORKING, Transition.ALL_SITES_REACHED, State.CONNECTION_WORKING, True),
    ]

    def evaluation_generator_function():
        for tick in expected_ticks[1:]:
            yield (tick.transition, tick.end_state, tick.is_terminal)

    evaluation_generator = evaluation_generator_function()
    mock_evaluator = MockEvaluator(evaluation_generator)
    steady_state = expected_ticks[0]

    machine = StateMachine(mock_evaluator, [steady_state])

    for i in range(1, len(expected_ticks) - 2):
        tick_list = machine.evaluate()
        expected_sublist = expected_ticks[0:i + 1]
        verify_tick_list(tick_list, expected_sublist)
        last_tick = expected_ticks[i]
        assert machine.is_terminal_state() == last_tick.is_terminal

    tick_list = machine.evaluate()
    verify_tick_list(tick_list, [expected_ticks[-2]])

    tick_list = machine.evaluate()
    verify_tick_list(tick_list, [expected_ticks[-1]])
