def calc_kernel(i, j, z_minus, z_plus):
    z_j = z_minus[j]
    z_i = z_plus[i]
    n = len(z_plus)
    denominator = z_i - z_j
    diagonal = (i + j == n - 1)

    if denominator == 0:
        if diagonal:
            return 0
        elif i + j < n - 1:
            return 1
        else:
            return -1
    else:
        res = (z_i + z_j) / denominator
        if res != 0:
            return res
        elif diagonal:
            return 0
        elif i + j < n - 1:
            return 1
        else:
            return -1

