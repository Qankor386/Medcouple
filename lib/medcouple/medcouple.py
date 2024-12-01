from lib.kernel_value.kernel_value import calc_kernel
from lib.median.median import find_median

def find_medcouple(data):
    data_sorted = sorted(data)
    median = find_median(data_sorted)

    X_minus = [x_j for x_j in data_sorted if x_j <= median]
    X_plus = [x_i for x_i in data_sorted if x_i >= median]

    matrix = []

    for x_j in X_minus:
        row = []
        for x_i in X_plus:
            if x_i != x_j:
                row.append(calc_kernel(x_i, x_j, median))
            else:
                row.append("NaN")
        matrix.append(row)

    kernel_values = [x for row in matrix for x in row if x != "NaN"]

    if not kernel_values:
        raise ValueError("Kernel values list is empty.")

    medcouple = find_median(kernel_values)


    # print("Sorted data: ", data_sorted)
    # print("Median: ", median)
    # print("X_minus:", [x_j for x_j in X_minus])
    # print("X_plus:", [x_i for x_i in X_plus])
    # print("\nMatrix:")
    # for row in matrix:
    #     print([x for x in row])
    # print("\nKernel values:", [x for x in kernel_values])
    # print("Kernel values sorted: ", sorted(kernel_values))
    # print("Medcouple: ", medcouple)

    return medcouple
