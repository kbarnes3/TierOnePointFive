import requests
import requests.exceptions
import requests_mock

from tieronepointfive.enums import State, Transition
from tieronepointfive.state_machine import StateMachineTick
from tieronepointfive.evaluation_helpers import HttpHelper
from ..mock_config import MockConfig

google = 'https://www.google.com'
bing = 'https://www.bing.com'


def _assert_ticks_equal(actual_tick, expected_tick):
    assert actual_tick.is_complete() == expected_tick.is_complete()
    assert actual_tick.is_steady() == expected_tick.is_steady()
    assert actual_tick.start_state == expected_tick.start_state
    assert actual_tick.transition == expected_tick.transition
    assert actual_tick.end_state == expected_tick.end_state
    assert actual_tick.is_terminal == expected_tick.is_terminal


def _test_http_helper(expected_transition, expected_end_state, expected_is_terminal):
    config = MockConfig
    helper = HttpHelper(config)
    start_tick = StateMachineTick(State.CONNECTION_WORKING)
    actual_tick = helper.evaluate(start_tick)
    expected_tick = StateMachineTick.create_completed(State.CONNECTION_WORKING, expected_transition, expected_end_state, expected_is_terminal)
    _assert_ticks_equal(actual_tick, expected_tick)


def test_http_helper_working_connection():
    with requests_mock.Mocker() as req_mock:
        req_mock.get(google, text='sure')
        req_mock.get(bing, text='sure')

        _test_http_helper(Transition.ALL_SITES_REACHED, State.CONNECTION_WORKING, True)


def test_http_helper_partially_working():
    with requests_mock.Mocker() as req_mock:
        req_mock.get(google, text='sure')
        req_mock.get(bing, exc=requests.exceptions.ConnectTimeout)

        _test_http_helper(Transition.SOME_SITES_REACHED, State.CONNECTION_FAILED, True)


def test_http_helper_bad_return_codes():
    with requests_mock.Mocker() as req_mock:
        req_mock.get(google, text='bad', status_code=400)
        req_mock.get(bing, text='bad', status_code=400)

        _test_http_helper(Transition.NO_SITES_REACHED, State.CONNECTION_FAILED, True)

