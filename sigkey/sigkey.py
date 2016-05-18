INFILE = 'sigkey.in'
OUTFILE = 'sigkey.out'


def task(fl):
    start = ord('a')
    end = ord('z')
    max_n = end - start + 1
    mask = (1 << max_n - 1) - 1
    seen = set()
    lines = fl.readlines()
    arr_len = len(lines)
    array = [None] * arr_len

    for i in xrange(arr_len):
        key = 0
        for c in lines[i][:-1]:
            key |= 1 << (ord(c) - start)
        array[i] = key

    array.sort(reverse=True)

    for i in xrange(arr_len):
        if i in seen:
            continue
        x = array[i]
        left = i + 1
        right = arr_len - 1
        expc = ((1 << x.bit_length()) - 1) ^ x
        while left <= right:
            middle = (left + right) // 2
            y = array[middle]
            if middle in seen or y < expc:
                right = middle - 1
            elif y > expc:
                left = middle + 1
            else:
                seen.add(middle)
                break

    return len(seen)


def main():
    # read
    with open(INFILE, 'r') as fl:
        count = int(fl.readline())
        result = task(fl)

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write(str(result))

if __name__ == '__main__':
    main()
