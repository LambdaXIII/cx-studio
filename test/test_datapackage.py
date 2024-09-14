import unittest

from cx_studio.core import DataPackage


class TestDataPackage(unittest.TestCase):
    def test_basic_props(self):
        a = DataPackage(test1=1, test2=2.2)
        a.test3 = 'hello'
        self.assertEqual(a.test1, a['test1'])
        self.assertEqual(a.test2, a['test2'])
        self.assertEqual(a.test3, a['test3'])

    def test_inner_package(self):
        data = {f'test{x}': int(x) for x in range(0, 10)}
        a = DataPackage(**data)
        for i in range(0,10):
            self.assertEqual(a[f'test{i}'],i)

        b = DataPackage()
        b.test_data = data
        self.assertTrue(isinstance(b.test_data, DataPackage))

        b["inner.basic"] = 'a'
        self.assertTrue(isinstance(b.inner,DataPackage))
        self.assertEqual(b.inner.basic,'a')
