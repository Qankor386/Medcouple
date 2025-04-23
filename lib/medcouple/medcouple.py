from lib.kernel.kernel import calc_kernel, count_leq
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

    print("\nOriginal data: ", data)
    print("Median: ", median)
    print("Sorted data - media: ", data_sorted)
    print("X_minus:", [x_c for x_c in z_minus])
    print("X_plus:", [x_r for x_r in z_plus])
    print("\nMatrix:")
    for row in matrix:
        print([x for x in row])

    header = matrix[0][1:]
    rows = [row[1:] for row in matrix[1:]]
    index = [row[0] for row in matrix[1:]]
    df = pd.DataFrame(rows, columns=header, index=index)

    print("\nFormated matrix:")
    print(df)
    print("\nValues: ", values)
    print("Medcouple: ", medcouple)

    return medcouple

def find_medcouple(data):

    data_sorted = sorted(data, reverse=True)
    median = find_median(data_sorted)

    for x in range(len(data_sorted)):
        data_sorted[x] -= median

    z_minus = [x_j for x_j in data_sorted if x_j <= 0]
    z_plus = [x_i for x_i in data_sorted if x_i >= 0]

    p = len(z_minus)
    q = len(z_plus)

    total = p * q
    k = total // 2

    h_low = -1
    h_high = 1
    eps = 1e-9

    while h_high - h_low > eps:
        h_mid = (h_low + h_high) / 2
        if count_leq(h_mid, z_minus, z_plus) <= k:
            h_low = h_mid
        else:
            h_high = h_mid

    return (h_high + h_low) / 2
