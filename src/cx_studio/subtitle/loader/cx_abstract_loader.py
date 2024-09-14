from abc import ABC, abstractmethod

from cx_studio.utils import detect_encoding
from ..cx_subtitle import Subtitle, SubtitleProcessor


class SubtitleLoader(ABC):
    def __init__(self, filename, encoding=None):
        self._filename = filename
        self._encoding = str(encoding)

    @property
    def encoding(self):
        if self._encoding and self._encoding != 'auto':
            return self._encoding
        return detect_encoding(self._filename)

    @abstractmethod
    def __enter__(self):
        return self

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

    @abstractmethod
    def subtitles(self):
        pass
