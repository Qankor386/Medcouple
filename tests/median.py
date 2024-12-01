import unittest
from lib.median.median import find_median


class TestFindMedian(unittest.TestCase):

    def test_odd_length(self):
        data = [24, 62, 37, 18, 96, 53, 11, 72, 80, 41, 5, 25, 63, 15, 91, 40, 10, 83, 47, 66, 39]
        result = find_median(data)
        self.assertEqual(result, 41)

    def test_even_length(self):
        data = [42, 17, 89, 58, 36, 95, 73, 11, 21, 64, 88, 45, 9, 67, 77, 18, 33, 71, 55, 94]
        result = find_median(data)
        self.assertEqual(result, 56.5)

    def test_float_values_odd(self):
        data = [43.96, 19.57, 70.42, 36.94, 96.06, 44.1, 34.21, 17.2, 54.77, 14.83, 55.01]
        result = find_median(data)
        self.assertEqual(result, 43.96)

    def test_empty_list(self):
        data = []
        with self.assertRaises(ValueError) as context:
            find_median(data)
        self.assertEqual(str(context.exception), "The list is empty.")
