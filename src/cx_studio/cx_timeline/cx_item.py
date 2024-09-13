from cx_core import DataPackage, Time, TimeRangeSupport


class Item(TimeRangeSupport):
    def __init__(self) -> None:
        super().__init__()
        self._start = Time()
        self._duration = Time()
        self._data = DataPackage()

    @property
    def start(self):
        return self._start

    @start.setter
    def set_start(self, value):
        assert isinstance(value, Time)
        self._start = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def set_duration(self, value):
        assert isinstance(value, Time)
        self._duration = value

    @property
    def end(self):
        return self.start + self.duration

    @end.setter
    def set_end(self, value):
        assert isinstance(value, Time)
        self.duration = value - self.start

    @property
    def data(self):
        return self._data
