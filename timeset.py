import datetime

# 時間の設定


class Timeset:

    _MILISECONDS_PER_SECOND = 1000

    def __init__(self):
        self._reset()

    def stop(self):
        if (self._duration is None):
            end = datetime.datetime.now()
            delta = end - self.start
            self._duration = int(delta.total_seconds() *
                                 Timeset._MILISECONDS_PER_SECOND)
        return self._duration

    def restart(self):
        ms = self.stop()
        self._reset()
        return ms

    def _reset(self):
        self.start = datetime.datetime.now()
        self._duration = None

    def get(self):
        if (self._duration is None):
            end = datetime.datetime.now()
            delta = end - self.start
            return int(delta.total_seconds() * Timeset._MILISECONDS_PER_SECOND)

        return 0
