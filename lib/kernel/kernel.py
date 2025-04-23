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


def count_leq(h_val, z_minus, z_plus):
    p = len(z_minus)
    q = len(z_plus)
    count = 0

    for i in range(q):
        low, high = 0, p
        while low < high:
            mid = (low + high) // 2
            if calc_kernel(i, mid, z_minus, z_plus) <= h_val:
                low = mid + 1
            else:
                high = mid
        count += low
    return count