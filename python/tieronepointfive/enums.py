from enum import auto, Enum, unique

@unique
class State(Enum):
    CONNECTION_WORKING = auto()
    CONNECTION_FAILED = auto()
    CABLE_MODEM_REBOOTING = auto()


@unique
class Transition(Enum):
    ALL_SITES_REACHED = auto()
    SOME_SITES_REACHED = auto()
    NO_SITES_REACHED = auto()
