from attr import attrs, attrib

from .base import SerializableStruct


def _conv_iid(iid):
    return iid.rstrip(b'\0')


@attrs(slots=True)
class OrderEntryRequest(SerializableStruct):
    account_id = attrib()
    strategy_id = attrib()
    oid = attrib()
    iid = attrib(converter=_conv_iid)
    action = attrib()
    quantity = attrib()
    price = attrib()
    time = attrib()

    fmt = '<HHI16sHIdQ'


@attrs(slots=True)
class OrderCancelRequest(SerializableStruct):
    account_id = attrib()
    strategy_id = attrib()
    oid = attrib()
    time = attrib()

    fmt = '<HHIQ'


@attrs(slots=True)
class OrderUpdate(SerializableStruct):
    account_id = attrib()
    strategy_id = attrib()
    oid = attrib()
    iid = attrib()
    action = attrib()
    quantity = attrib()
    price = attrib()
    time = attrib()
    type = attrib()
    filled = attrib()
    remaining = attrib()
    canceled = attrib()
    fill_price = attrib()

    fmt = '<HHI16sHIdQHIIId'


