from tieronepointfive.enums import State
from tieronepointfive.state_machine import StateMachineTick
from tieronepointfive.evaluation_helpers import HttpHelper

helper = HttpHelper()
start_tick = StateMachineTick(State.CONNECTION_WORKING)
end_tick = helper.evaluate(start_tick)
print(end_tick)
