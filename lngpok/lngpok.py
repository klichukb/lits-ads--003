INFILE = 'lngpok.in'
OUTFILE = 'lngpok.out'


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
        less = [v for v in array if v < pivot]
        more = [v for v in array if v > pivot]
        equal = array.count(pivot) * [pivot]
        return adapt_quick_sort(less) + equal + adapt_quick_sort(more)


def task(array):
    """
    Sorts, then incrementally moves forward, attempting to build sequences in optimistic fashion
    as soon as possible using jokers.
    """
    arr_len = len(array)
    array = adapt_quick_sort(array)

    i = 0
    seq = max_seq = 1
    cut = None

    while i < arr_len and array[i] == 0:
        i += 1

    buffer = jokers = i

    if jokers == arr_len:
        return arr_len
    if jokers == arr_len - 1:
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
