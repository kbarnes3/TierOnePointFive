from enum import Enum, unique


@unique
class State(Enum):
    def __str__(self):
        return self.name

    NO_DATA_FILE = 0
    BAD_DATA_FILE = 1
    FRESH_DATA_FILE = 2
    CONNECTION_WORKING = 3
    CONNECTION_FAILED = 4
    CABLE_MODEM_REBOOT_NEEDED = 5
    CABLE_MODEM_REBOOTING = 6
    CABLE_MODEM_REBOOT_FAILED = 7
    ROUTER_REBOOT_NEEDED = 8
    ROUTER_REBOOTING = 9
    ROUTER_REBOOT_FAILED = 10
    EMAIL_QUEUED = 11


@unique
class Transition(Enum):
    def __str__(self):
        return self.name

    DATA_FILE_CREATED = 0
    ALL_SITES_REACHED = 1
    SOME_SITES_REACHED = 2
    NO_SITES_REACHED = 3
    CABLE_MODEM_POWER_CYCLED = 4
    CABLE_MODEM_POWER_CYCLE_FAILED = 5
    ROUTER_POWER_CYCLED = 6
    ROUTER_POWER_CYCLE_FAILED = 7
    EMAIL_SENT = 8
    EMAIL_FAILED = 9
