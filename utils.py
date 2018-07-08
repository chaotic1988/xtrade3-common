import time
import datetime


def timestamp():
    return int(time.time()*1000)


def timestamp_to_datetime(ts):
    return datetime.datetime.fromtimestamp(ts/1000.0)
