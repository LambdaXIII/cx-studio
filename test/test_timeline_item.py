import unittest
from cx_studio.timeline import Item


class TestTimelineItem(unittest.TestCase):
    def test_constructing(self):
        a = Item()
        self.assertEqual(a.start,0)
        self.assertEqual(a.duration,0)
        a.start = 1000
        a.duration = 1000
        self.assertEqual(a.start,1000)
        self.assertEqual(a.duration,1000)
        self.assertEqual(a.end,2000)
        b = Item.from_time_range(a)
        self.assertEqual(b.start,a.start)
        self.assertEqual(b.duration,a.duration)
        b.end = 1500
        self.assertEqual(b.duration,500)

    def test_intersection(self):
        a = Item(1000,1000)
        b = Item(500,3000)
        c = Item(2000,1000)
        d = Item(5000,100)
        self.assertTrue(a.intersects(b))
        self.assertTrue(b.intersects(c))
        self.assertFalse(a.intersects(d))
