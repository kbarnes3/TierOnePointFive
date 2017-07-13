import requests
import requests_mock

from tieronepointfive.enums import State, Transition
from tieronepointfive.state_machine import StateMachineTick
from tieronepointfive.evaluation_helpers import HttpHelper


def _assert_ticks_equal(actual_tick, expected_tick):
    assert actual_tick.is_complete() == expected_tick.is_complete()
    assert actual_tick.is_steady() == expected_tick.is_steady()
    assert actual_tick.start_state == expected_tick.start_state
    assert actual_tick.transition == expected_tick.transition
    assert actual_tick.end_state == expected_tick.end_state
    assert actual_tick.is_terminal == expected_tick.is_terminal


def test_http_helper_working_connection():
    with requests_mock.Mocker() as req_mock:
        req_mock.get('https://www.google.com', text='sure')
        req_mock.get('https://www.bing.com', text='sure')

        helper = HttpHelper()
        start_tick = StateMachineTick(State.CONNECTION_WORKING)
        actual_tick = helper.evaluate(start_tick)
        expected_tick = StateMachineTick.create_completed(State.CONNECTION_WORKING, Transition.ALL_SITES_REACHED, State.CONNECTION_WORKING, True)
        _assert_ticks_equal(actual_tick, expected_tick)

