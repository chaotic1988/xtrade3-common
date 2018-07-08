import datetime
import heapq
import time
import zmq

DEFAULT_POLL_TIMEOUT = 100

_mono = time.perf_counter


class _Timer:
    __slots__ = ['delay', 'times', 'next_fire_time', 'callback']

    def __init__(self, delay, times, callback):
        self.delay = delay
        self.times = times
        self.next_fire_time = _mono() + delay
        self.callback = callback

    def __lt__(self, other):
        return self.next_fire_time < other.next_fire_time


class XLoop:

    def __init__(self):
        self._stop = False
        self._timers = []
        self._handlers = {}
        self._poller = zmq.Poller()

    def add_handler(self, socket, handler):
        self._handlers[socket] = handler
        self._poller.register(socket, zmq.POLLIN)

    def add_timer(self, callback, delay, times):
        assert (callable(callback))
        t = _Timer(delay, times, callback)
        heapq.heappush(self._timers, t)

    def run_in(self, callback, seconds):
        self.add_timer(callback, seconds, 1)

    def run_at(self, callback, at):
        now = datetime.datetime.now()
        delta = (at - now).total_seconds()

        self.add_timer(callback, delta, 1)

    def run_periodically(self, callback, interval, times=-1):
        self.add_timer(callback, interval, times)

    def start(self):
        timers = self._timers
        handlers = self._handlers
        poller = self._poller

        while not self._stop:
            if timers:
                due_timers = []
                now = _mono()
                while timers:
                    if now >= timers[0].next_fire_time:
                        t = heapq.heappop(timers)
                        due_timers.append(t)
                    else:
                        break

                for t in due_timers:
                    t.callback()
                    if t.times > 0:
                        t.times -= 1
                    if t.times != 0:
                        t.next_fire_time += t.delay
                        heapq.heappush(timers, t)

            if timers:
                timeout = (timers[0].next_fire_time - _mono()) * 1000
                timeout = max(0, timeout)
            else:
                timeout = DEFAULT_POLL_TIMEOUT

            events = poller.poll(timeout)
            for socket, event in events:
                if event == zmq.POLLIN:
                    handlers[socket](socket)

    def stop(self):
        self._stop = True
