from ..core import TimeRangeSupport, Time, DataPackage


class Track(TimeRangeSupport):
    def __init__(self) -> None:
        super().__init__()
        self._items: list[TimeRangeSupport] = []
        self._data = DataPackage()

    @property
    def start(self) -> Time:
        return Time(0)

    @property
    def duration(self) -> Time:
        if len(self.items) == 0:
            return Time(0)
        else:
            return self._items[-1].end

    @property
    def items(self) -> list[TimeRangeSupport]:
        return self._items

    @property
    def data(self):
        return self._data
