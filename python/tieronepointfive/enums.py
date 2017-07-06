from enum import auto, Enum, unique

@unique
class State(Enum):
    CONNECTION_WORKING = auto()
    CONNECTION_FAILED = auto()
    CABLE_MODEM_REBOOT_NEEDED = auto()
    CABLE_MODEM_REBOOTING = auto()
    ROUTER_REBOOT_NEEDED = auto()
    ROUTER_REBOOTING = auto()
    EMAIL_QUEUED = auto()


@unique
class Transition(Enum):
    ALL_SITES_REACHED = auto()
    SOME_SITES_REACHED = auto()
    NO_SITES_REACHED = auto()
    CABLE_MODEM_POWER_CYCLED = auto()
    CABLE_MODEM_POWER_CYCLE_FAILED = auto()
    ROUTER_POWER_CYCLED = auto()
    ROUTER_POWER_CYCLE_FAILED = auto()
    EMAIL_SENT = auto()
    EMAIL_FAILED = auto()
