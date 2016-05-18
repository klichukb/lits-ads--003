INFILE = 'sigkey.in'
OUTFILE = 'sigkey.out'


def task(fl):
    start = ord('a')
    end = ord('z')
    max_n = end - start + 1
    mask = (1 << max_n - 1) - 1
    lines = fl.readlines()
    arr_len = len(lines)
    seen = set()
    array = [None] * arr_len

    for i in xrange(arr_len):
        key = 0
        for c in lines[i][:-1]:
            key |= 1 << (ord(c) - start)
        array[i] = key
    array.sort(reverse=True)

    count = 0
    for i in xrange(arr_len):
        x = array[i]
        if x in seen:
            seen.remove(x)
            count += 1
            continue
        expc = ((1 << x.bit_length()) - 1) ^ x
        seen.add(expc)
    return count


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
