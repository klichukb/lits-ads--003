INFILE = 'hamstr.in'
OUTFILE = 'hamstr.out'


def sum_first_k(array, k):
    """
    Calculates sum of first K elements recursively (quick select).
    """
    length = len(array)

    if length == 0:
        return 0
    elif length == 1:
        return array[0]

    pivot = array[len(array) / 2]
    less = [v for v in array if v < pivot]
    less_cnt = len(less)

    if less_cnt == k:
        return sum(less) + pivot
    elif less_cnt > k:
        return sum_first_k(less, k)

    k -= less_cnt
    equal_cnt = array.count(pivot)
    if equal_cnt > k:
        return k * pivot

    more = [v for v in array if v > pivot]
    return sum(less) + equal_cnt * pivot + sum_first_k(more, k - equal_cnt)


def task(total, array):
    arr_len = len(array)
    aux = [None] * arr_len
    left = 0
    right = arr_len - 1

    while left <= right:
        middle = left + (right - left) // 2
        aux[:] = [array[j][0] + middle * array[j][1] for j in xrange(arr_len)]
        if sum_first_k(aux, middle) > total:
            right = middle - 1
        else:
            left = middle + 1
    return left


def main():
    # read
    with open(INFILE, 'r') as fl:
        total = int(fl.readline())
        count = int(fl.readline())
        array = [[int(h) for h in fl.readline().split()] for i in range(count)]

    result = task(total, array)

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write(str(result))

if __name__ == '__main__':
    main()
