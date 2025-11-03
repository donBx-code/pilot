import unittest

from pilot.sample import add


class TestSample(unittest.TestCase):
    def testpass1(self):
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(3, 6), 9)
        self.assertEqual(add(3, 8), 11)


class TestSample2(unittest.TestCase):
    def testpass1(self):
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(3, 6), 9)
        self.assertEqual(add(3, 8), 12)

if __name__ == '__main__':
    unittest.main()