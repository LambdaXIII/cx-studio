from dataclasses import dataclass
from functools import lru_cache

from ..core import DataPackage, Time


@dataclass(order=True, frozen=True)
class Subtitle:
    start: Time
    end: Time
    content: str
    attachment: DataPackage = None

    @property
    @lru_cache
    def duration(self):
        return self.end - self.start
