INFILE = 'lngpok.in'
OUTFILE = 'lngpok.out'


def merge_sort(seq, seq_len):
    """
    Flat bottom-up merge sort.
    """
    aux = [None] * len(seq)
    if seq_len == 1:
        return seq

    step = 1
    while step < seq_len:
        step <<= 1
        for i in range(0, seq_len, step):
            right = min(i + step - 1, seq_len - 1)
            if i == right:
                aux[i] = seq[i]
                continue
            elif i + 1 == right:
                if seq[i] <= seq[right]:
                    aux[i], aux[right] = seq[i], seq[right]
                else:
                    aux[i], aux[right] = seq[right], seq[i]
                continue
            middle = i + step // 2 - 1
            pos = left_pos = i
            right_pos = middle + 1
            while pos <= right:
                if left_pos <= middle and (right_pos > right or seq[left_pos] < seq[right_pos]):
                    aux[pos] = seq[left_pos]
                    left_pos += 1
                else:
                    aux[pos] = seq[right_pos]
                    right_pos += 1
                pos += 1
        seq, aux = aux, seq
    return seq


def task(array):
    """
    Sorts, then incrementally moves forward, attempting to build sequences in optimistic fashion
    as soon as possible using jokers.
    """
    arr_len = len(array)
    array = merge_sort(array, arr_len)

    i = 0
    seq = max_seq = 1
    cut = None

    while i < arr_len and array[i] == 0:
        i += 1

    buffer = jokers = i
    if jokers == arr_len:
        return arr_len

    if i == arr_len - 1:
        return jokers + 1

    i += 1

    while i < arr_len:
        diff = array[i] - array[i - 1]
        if diff < 2:
            if diff == 1:
                seq += 1
            i += 1
            continue
        i += 1

        left = buffer - diff + 1
        if left >= 0:
            seq += diff
            buffer = left
            if cut is None:
                cut = i
        else:
            # sequence break
            seq += buffer
            buffer = jokers
            if seq > max_seq:
                max_seq = seq
            if cut is not None:
                i = cut
            seq = 1
            cut = None

    if buffer:
        seq += buffer
    if seq > max_seq:
        max_seq = seq
    return max_seq


def main():
    # read
    with open(INFILE, 'r') as fl:
        array = [int(h) for h in fl.readline().split()]

    result = task(array)

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write(str(result))

if __name__ == '__main__':
    main()
