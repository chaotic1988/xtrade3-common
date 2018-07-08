from enum import IntEnum


class PositionSide(IntEnum):
    LONG = 0
    SHORT = 1


class OrderAction(IntEnum):
    BUY = 0
    SELL = 1


class OrderStatus(IntEnum):
    CREATED = 0
    ACCEPTED = 1
    REJECTED = 2
    COMPLETE = 3
    CANCELED = 4


class OrderUpdateType(IntEnum):
    ACCEPT = 0
    REJECT = 1
    FILL = 2
    CANCEL = 3

