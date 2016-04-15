INFILE = 'discnt.in'
OUTFILE = 'discnt.out'

# Merge sort (recursive)
# O(n logn)


def merge_sort(seq):
    """
    A convenience function for Merge Sort.
    """
    aux = [None] * len(seq)
    _merge_sort(seq, 0, len(seq) - 1, aux)


def _merge_sort(seq, left, right, aux):
    if left == right:
        return
    middle = (left + right) // 2
    left_pos = left
    right_pos = middle + 1
    _merge_sort(seq, left_pos, middle, aux)
    _merge_sort(seq, right_pos, right, aux)

    pos = left
    while pos <= right:
        if left_pos <= middle and (right_pos > right or seq[left_pos] > seq[right_pos]):
            aux[pos] = seq[left_pos]
            left_pos += 1
        else:
            aux[pos] = seq[right_pos]
            right_pos += 1
        pos += 1

    seq[left:right+1] = aux[left:right+1]


def task(array, discount):
    arr_len = len(array)
    mod = 1 - discount / 100.0
    offset = arr_len / 3 - 1

    merge_sort(array)

    result = 0
    for i in xrange(arr_len):
        if i <= offset:
            result += array[i] * mod
        else:
            result += array[i]
    return result

def main():
    # read
    with open(INFILE, 'r') as fl:
        array = [int(token) for token in fl.readline().split()]
        discount = int(fl.readline())

    # do
    result = task(array, discount)

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write(repr(result))


if __name__ == '__main__':
    main()
