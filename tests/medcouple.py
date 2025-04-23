import unittest
from lib.medcouple.medcouple import find_medcouple, find_medcouple_naive


class TestFindMedcouple(unittest.TestCase):

    def test_find_medcouple_even(self):
        data = [1, 2, 3, 4, 7, 8]
        result = find_medcouple_naive(data)
        self.assertEqual(result, 0.2857142857142857)

    def test_find_medcouple_odd(self):
        data = [1, 2, 8, 9, 10]
        result = find_medcouple_naive(data)
        self.assertEqual(result, -0.5555555555555556)