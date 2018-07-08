from attr import attrs, attrib

from .base import SerializableStruct

__all__ = [
    'OrderEntryRequest',
    'OrderCancelRequest',
    'OrderUpdate'
]


def _conv_iid(iid):
    return iid.rstrip(b'\0')


@attrs(slots=True)
class OrderEntryRequest(SerializableStruct):
    eid = 16
    fmt = '<HHI16sHIdQ'

    account_id = attrib()
    strategy_id = attrib()
    oid = attrib()
    iid = attrib(converter=_conv_iid)
    action = attrib()
    quantity = attrib()
    price = attrib()
    time = attrib()


@attrs(slots=True)
class OrderCancelRequest(SerializableStruct):
    eid = 17
    fmt = '<HHIQ'

    account_id = attrib()
    strategy_id = attrib()
    oid = attrib()
    time = attrib()


@attrs(slots=True)
class OrderUpdate(SerializableStruct):
    eid = 18
    fmt = '<HHI16sHIdQHIIId'

    account_id = attrib()
    strategy_id = attrib()
    oid = attrib()
    iid = attrib(converter=_conv_iid)
    action = attrib()
    quantity = attrib()
    price = attrib()
    time = attrib()
    type = attrib()
    filled = attrib()
    remaining = attrib()
    canceled = attrib()
    fill_price = attrib()
