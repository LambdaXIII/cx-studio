from abc import ABC, abstractmethod
from typing import Union

from ..cx_subtitle import Subtitle


class SubtitleProcessor(ABC):

    @abstractmethod
    def __call__(self, subtitle: Subtitle) -> Union[Subtitle | None]:
        return subtitle
