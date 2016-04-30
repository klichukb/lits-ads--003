import sys

INFILE = 'hamstr.in'
OUTFILE = 'hamstr.out'


def merge_sort(array, aux, arr_len):
    right = arr_len
    if arr_len < 2:
        return array

    step = 1

    while step < arr_len:
        step <<= 1
        for i in xrange(0, arr_len, step):
            right = min(i + step - 1, arr_len - 1)
            if i == right:
                aux[i] = array[i]
                continue
            elif i + 1 == right:
                if array[i] < array[right]:
                    aux[i], aux[right] = array[i], array[right]
                else:
                    aux[i], aux[right] = array[right], array[i]
                continue
            middle = i + step // 2 - 1
            pos = left_pos = i
            right_pos = middle + 1
            while pos <= right:
                if left_pos <= middle and (right_pos > right or array[left_pos] < array[right_pos]):
                    aux[pos] = array[left_pos]
                    left_pos += 1
                else:
                    aux[pos] = array[right_pos]
                    right_pos += 1
                pos += 1
        array, aux = aux, array
    return array


def task(total, array):
    arr_len = len(array)
    aux = [None] * arr_len
    sort_aux = [None] * arr_len
    left = 0
    right = arr_len - 1

    while left <= right:
        middle = left + (right - left) // 2
        aux[:] = [array[j][0] + middle * array[j][1] for j in xrange(arr_len)]
        _aux = merge_sort(aux, sort_aux, arr_len)
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
