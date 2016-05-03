import sys

INFILE = 'hamstr.in'
OUTFILE = 'hamstr.out'


def insert_sort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i
        while j > 0 and array[j - 1] > value:
            array[j] = array[j - 1]
            j -= 1
        array[j] = value
    return array


def adapt_quick_sort(array):
    length = len(array)
    if length <= 1:
        return array
    if length <= 20:
        return insert_sort(array)
    else:
        pivot = array[0]
        less, more, equal = [], [], []
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                more.append(x)
        return adapt_quick_sort(less) + equal + adapt_quick_sort(more)


def task(total, array):
    arr_len = len(array)
    aux = [None] * arr_len
    left = 0
    right = arr_len - 1

    while left <= right:
        middle = left + (right - left) // 2
        aux[:] = [array[j][0] + middle * array[j][1] for j in xrange(arr_len)]
        _aux = adapt_quick_sort(aux)
        nsum = sum(_aux[:middle + 1])
        if nsum > total:
            right = middle - 1
        elif nsum <= total:
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
