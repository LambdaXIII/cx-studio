import re

from cx_studio.core import Time
from .cx_abstract_loader import SubtitleLoader
from ..cx_subtitle import Subtitle


class TxtLoader(SubtitleLoader):
    DURATION_PER_CHAR = 120
    MIN_DURATION_PER_LINE = 2000
    TS_PATTERN = r'\s*\d{2}:\d{2}:\d{2}.\d{3}\s*'

    def __init__(self, filename, encoding=None,
                 duration_per_char: int = None,
                 min_duration_per_line: int = None):
        super().__init__(filename, encoding)
        self._file = None
        self._encoding = encoding
        self.duration_per_char = duration_per_char or self.DURATION_PER_CHAR
        self.min_duration_per_line = (
                min_duration_per_line or self.MIN_DURATION_PER_LINE)
        self.__prev_time = Time()

    def __enter__(self):
        self._file = open(self._filename, 'r', encoding=self.encoding)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file:
            self._file.close()
        return False

    def subtitles(self):
        for line in self._file:
            content = re.sub(self.TS_PATTERN, '', line)
            duration = max(len(content) * self.duration_per_char,
                           self.min_duration_per_line)
            yield Subtitle(
                start=self.__prev_time,
                end=self.__prev_time + Time(duration),
                content=content
            )
            self.__prev_time += duration
