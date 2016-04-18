INFILE = 'discnt.in'
OUTFILE = 'discnt.out'


def merge_sort(seq):
    aux = [None] * len(seq)
    _merge_sort(seq, 0, len(seq) - 1, aux)


def _merge_sort(seq, left, right, aux):
    seq_len = len(seq)
    if left == right:
        return

    step = 1
    while step < seq_len:
        step <<= 1
        for i in range(0, seq_len, step):
            right = min(i + step - 1, seq_len - 1)
            if i == right:
                aux[i] = seq[i]
                continue
            elif i + 1 == right:
                if seq[i] >= seq[right]:
                    aux[i], aux[right] = seq[i], seq[right]
                else:
                    aux[i], aux[right] = seq[right], seq[i]
                continue
            middle = i + step // 2 - 1
            pos = left_pos = i
            right_pos = middle + 1
            while pos <= right:
                if left_pos <= middle and (right_pos > right or seq[left_pos] > seq[right_pos]):
                    aux[pos] = seq[left_pos]
                    left_pos += 1
                else:
                    aux[pos] = seq[right_pos]
                    right_pos += 1
                pos += 1
        seq, aux = aux, seq


def task(array, discount):
    arr_len = len(array)
    mod = 1 - discount / 100.0

    # a shortcut, no discount = total sum.
    if discount == 0:
        return sum(array)

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

    result = task(array, discount)

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write('{:.2f}'.format(result))


if __name__ == '__main__':
    main()
