import unittest
from lib.medcouple.medcouple import find_medcouple_naive, find_medcouple_fast
from lib.runtime.runtime import measure_runtime
from tests.medcouple import TestFindMedcouple
from tests.median import TestFindMedian
from lib.runtime import runtime
import random
from lib.median.median import find_low_median

def generate_test_data(sizes, seed=8):
    random.seed(seed)
    return {n: [random.uniform(-10, 10) for _ in range(n)] for n in sizes}

sizes = [10, 50, 100, 200, 500, 1000]
data = generate_test_data(sizes)

test_data = [4, 2, 0, 3, 1, 5, 3]
test_data2 = [7, 3, 4, 5, 2, 0, 8]
test_data3 = [8, 10, 3, 5, 2, 7, 0, 1, 3, 4]


if __name__ == '__main__':

    print("Naive MedCouple")
    print("\nMedcouple: ", find_medcouple_naive(test_data3))

    print("Fast MedCouple")
    print("\nFast MedCouple: ", find_medcouple_fast(test_data3))

    # unittest.main()

