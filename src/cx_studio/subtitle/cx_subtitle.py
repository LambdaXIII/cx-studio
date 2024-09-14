from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import lru_cache

from ..core import Time, DataPackage


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


class SubtitleProcessor(ABC):
    @abstractmethod
    def __call__(self, subtitle: Subtitle) -> Subtitle:
        pass


