from attr import attrs, attrib

from .base import SerializableStruct


def _conv_iid(iid):
    return iid.rstrip(b'\0')


@attrs(slots=True, cmp=False)
class OrderEntryRequest(SerializableStruct):
    account_id = attrib()
    strategy_id = attrib()
    oid = attrib()
    iid = attrib(converter=_conv_iid)
    action = attrib()
    quantity = attrib()
    price = attrib()

    fmt = '<HHI16sHId'


@attrs(slots=True, cmp=False)
class OrderCancelRequest:
    account_id = attrib()
    strategy_id = attrib()
    oid = attrib()

    fmt = '<HHI'


@attrs(slots=True, cmp=False)
class OrderReceipt:
    account_id = attrib()
    strategy_id = attrib()
    oid = attrib()
    iid = attrib(converter=_conv_iid)
    action = attrib()
    quantity = attrib()
    price = attrib()


@attrs(slots=True, cmp=False)
class OrderUpdate:
    account_id = attrib()
    strategy_id = attrib()
    oid = attrib()
    time = attrib()
    type = attrib()
    filled = attrib()
    remaining = attrib()
    canceled = attrib()
    fill_price = attrib()

    fmt = '<HHIQIIIId'

