"""Sample tests"""

from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Testing adding numbers"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Testing subtracting numbers"""

        res = calc.subtract(10, 5)
        self.assertEqual(res, 5)
