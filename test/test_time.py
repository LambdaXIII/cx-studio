import unittest

from cx_studio.core import Time


class TestCxTime(unittest.TestCase):
    def setUp(self):
        self.a = Time(1000.12)
        self.b = Time(512)

    def test_millisecond(self):
        self.assertEqual(self.a.milliseconds, 1000)
        self.assertEqual(self.b.milliseconds, 512)

    def test_calculates(self):
        self.assertEqual(self.a + self.b, Time(1512))
        self.assertEqual(self.a + 512, Time(1512))
        self.assertEqual(self.a - 500, Time(500))
        self.assertEqual(self.a * 2, Time(2000))
        self.assertEqual(self.a / 10, Time(100))
