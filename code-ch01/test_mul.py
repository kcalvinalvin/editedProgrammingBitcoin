from eccCh01 import FieldElement
from unittest import TestCase

class FieldElementTest(TestCase):
    def test_mul(self):
        a = FieldElement(24, 31)
        b = FieldElement(19, 31)
        self.assertEqual(a * b, FieldElement(22, 31))
