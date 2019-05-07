from unittest import TestCase
from eccCh02 import Point

class PointTest(TestCase):
    def test_add2(self):
        a = Point(x=-1, y=-1, a=5, b=7)
        self.assertEqual(a + a, Point(x=18, y=77, a=5, b=7))
