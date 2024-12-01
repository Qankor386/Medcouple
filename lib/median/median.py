def find_median(data):
    if not data:
        raise ValueError("The list is empty.")

    sorted_list = sorted(data)
    n = len(sorted_list)

    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        med1 = sorted_list[n // 2 - 1]
        med2 = sorted_list[n // 2]

        return (med1 + med2) / 2
