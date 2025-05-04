from lib.kernel.kernel import calc_kernel
from lib.median.median import find_median
import pandas as pd

def find_medcouple_naive(data):

    data_sorted = sorted(data, reverse=True)
    median = find_median(data_sorted)

    for x in range(len(data_sorted)):
        data_sorted[x] -= median

    z_minus = [x_j for x_j in data_sorted if x_j <= 0]
    z_plus = [x_i for x_i in data_sorted if x_i >= 0]

    matrix = []
    header = [" "] + z_minus
    matrix.append(header)

    for i, x_i in enumerate(z_plus):
        row = [x_i]
        for j, x_j in enumerate(z_minus):
            value = calc_kernel(i, j, z_minus, z_plus)
            row.append(value)
        matrix.append(row)

    values = sorted([value for row in matrix[1:] for value in row[1:]], reverse=True)
    medcouple = find_median(values)

    # print("\nOriginal data: ", data)
    # print("Median: ", median)
    # print("Sorted data - media: ", data_sorted)
    # print("X_minus:", [x_c for x_c in z_minus])
    # print("X_plus:", [x_r for x_r in z_plus])
    # print("\nMatrix:")
    # for row in matrix:
    #     print([x for x in row])

    header = matrix[0][1:]
    rows = [row[1:] for row in matrix[1:]]
    index = [row[0] for row in matrix[1:]]
    df = pd.DataFrame(rows, columns=header, index=index)

    # print("\nFormated matrix:")
    # print(df)
    # print("\nValues: ", values)
    # print("Medcouple: ", medcouple)

    return medcouple


def find_medcouple_fast(data):

    data_sorted = sorted(data, reverse=True)
    # print("sorted data: ", data_sorted)

    median = find_median(data_sorted)
    # print("median: ", median)

    for x in range(len(data_sorted)):
        data_sorted[x] -= median
    # print("data - median: ", data_sorted)

    z_minus = [x_j for x_j in data_sorted if x_j <= 0]
    z_plus = [x_i for x_i in data_sorted if x_i >= 0]

    k = len(z_minus)
    l = len(z_plus)
    m = k * l
    # print("z_minus: ", z_minus)
    # print("z_plus: ", z_plus)
    # print("number of values: ", m)

    kernel_matrix = [[calc_kernel(i, j, z_minus, z_plus) for j in range(k)] for i in range(l)]

    def divide_values(pivot):
        less = equal = greater = 0
        for i in range(l):
            for j in range(k):
                val = kernel_matrix[i][j]
                if val < pivot:
                    less += 1
                elif val > pivot:
                    greater += 1
                else:
                    equal += 1
        return less, equal, greater

    def find_kth(kth):
        low = -1
        high = 1
        eps = 1e-10

        while high - low > eps:
            mid = (low + high) / 2
            less, equal, greater = divide_values(mid)
            if less <= kth < less + equal:
                return mid
            elif kth < less:
                high = mid
            else:
                low = mid

        return (low + high) / 2


    if m % 2 == 1:
        kth = m // 2
        h = find_kth(kth)
        # print("k (odd):", kth)
        # print("h:", h)

        return h
    else:
        k1 = (m - 1) // 2
        k2 = m // 2
        h1 = find_kth(k1)
        h2 = find_kth(k2)
        # print("k1: ", k1)
        # print("k2: ", k2)
        # print("h1: ", h1)
        # print("h2: ", h2)

        return (h1 + h2) / 2

