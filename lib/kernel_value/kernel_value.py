def calc_kernel(x_i, x_j, m):
    h = ((x_i - m) - (m - x_j)) / (x_i - x_j)

    return h