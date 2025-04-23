import unittest
from lib.medcouple.medcouple import find_medcouple, find_medcouple_naive
from lib.runtime.runtime import measure_runtime
from tests.medcouple import TestFindMedcouple
from tests.median import TestFindMedian
from lib.runtime import runtime
import random

def generate_test_data(sizes, seed=8):
    random.seed(seed)
    return {n: [random.uniform(-10, 10) for _ in range(n)] for n in sizes}

sizes = [10, 50, 100, 500, 1000]
data = generate_test_data(sizes)
test_data = [4, 3, 3, 2, 1]


if __name__ == '__main__':

    medcouple = measure_runtime(lambda: find_medcouple_naive(test_data))
    print("Time: ", medcouple, "s")

    # for size, d in data.items():
    #     duration = measure_runtime(lambda: find_medcouple_naive(d))
    #     print(f"Naive algoritm - Size: {size}, Time: {duration:.6f} s")

    print("\nFast MedCouple: ", find_medcouple(test_data))

    unittest.main()