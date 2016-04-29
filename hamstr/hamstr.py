import sys

INFILE = 'hamstr.in'
OUTFILE = 'hamstr.out'


def merge_sort(array, aux, arr_len, index=None):
    """
    Ugly but optimal merge sort.
    Use `index` in order specify array index to sort by in case array is array of lists.
    """
    right = arr_len
    if arr_len < 2:
        return array

    step = 1

    while step < arr_len:
        step <<= 1
        for i in range(0, arr_len, step):
            right = min(i + step - 1, arr_len - 1)
            if i == right:
                aux[i] = array[i]
                continue
            elif i + 1 == right:
                # ugly implementation of support for different compare keys
                ki = array[i]
                kr = array[right]
                if index is not None:
                    ki = ki[index]
                    kr = kr[index]
                if ki <= kr:
                    aux[i], aux[right] = array[i], array[right]
                else:
                    aux[i], aux[right] = array[right], array[i]
                continue
            middle = i + step // 2 - 1
            pos = left_pos = i
            right_pos = middle + 1
            while pos <= right:
                # ugly implementation of support for different compare keys
                if left_pos <= middle and (
                        right_pos > right or
                        (array[left_pos] if index is None else array[left_pos][index]) <
                        (array[right_pos] if index is None else array[right_pos][index])):
                    aux[pos] = array[left_pos]
                    left_pos += 1
                else:
                    aux[pos] = array[right_pos]
                    right_pos += 1
                pos += 1
        array, aux = aux, array
    return array

def get_approx_k(array, aux, arr_len, total):
    """
    Attempt to get approximate K position of maximum items that is not higher than `total`.
    """
    array = merge_sort(array, aux, arr_len, 1)

    sum_g = 0
    sum_total = 0
    for i in xrange(arr_len):
        sum_total += sum_g + array[i][1] * i + array[i][0]
        sum_g += array[i][1]
        if sum_total > total:
            return i - 1
    return i


def task(total, array):
    arr_len = len(array)
    aux = [None] * arr_len
    sort_aux = [None] * arr_len
    nmin = get_approx_k(array, aux, arr_len, total)

    for i in xrange(nmin, arr_len):
        for j in xrange(arr_len):
            aux[j] = array[j][0] + i * array[j][1]
        _aux = merge_sort(aux, sort_aux, arr_len)
        if sum(_aux[:i + 1]) > total:
            return i
    return arr_len


def main():
    # read
    with open(INFILE, 'r') as fl:
        total = int(fl.readline())
        count = int(fl.readline())
        array = [tuple(int(h) for h in fl.readline().split()) for i in range(count)]

    result = task(total, array)

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write('{:.2f}'.format(result))

if __name__ == '__main__':
    main()
