from typing import Callable

from .cx_subtitle_processor import SubtitleProcessor
from ..cx_subtitle import Subtitle


class SubtitleChainProcessor(SubtitleProcessor):
    def __init__(self, *processors: list[Callable]):
        super().__init__()
        self.processors = []
        self.processors += processors

    def append(self, processor: Callable[[Subtitle], Subtitle]):
        self.processors.append(processor)
        return self

    def __call__(self, subtitle: Subtitle):
        result = subtitle
        for p in self.processors:
            result = p(result)
            if result is None:
                break
        return result
