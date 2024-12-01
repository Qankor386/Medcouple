import unittest
from lib.medcouple.medcouple import find_medcouple
from tests.medcouple import TestFindMedcouple
from tests.median import TestFindMedian

data = [1, 2, 3, 4, 7, 8]
data2 = [1, 2, 8, 9, 10]

if __name__ == '__main__':
    medcouple = find_medcouple(data)
    print("Medcouple: ", medcouple)

    medcouple = find_medcouple(data2)
    print("Medcouple: ", medcouple)

    unittest.main()
