INFILE = 'sigkey.in'
OUTFILE = 'sigkey.out'


def task(keys):
    start = ord('a')
    end = ord('z')
    max_n = end - start + 1
    arr_len = len(keys)
    seen = set()
    array = [None] * arr_len

    for i in xrange(arr_len):
        key = 0
        for c in keys[i][:-1]:  # cut `\n`
            key |= 1 << (ord(c) - start)
        array[i] = key

    # start from most problematic keys..
    array.sort(reverse=True)

    count = 0
    for x in array:
        if x in seen:
            seen.remove(x)
            count += 1
            continue
        # regsiter the key, that `x` needs, for further lookup
        match_key = ((1 << x.bit_length()) - 1) ^ x
        seen.add(match_key)
    return count


def main():
    # read
    with open(INFILE, 'r') as fl:
        count = int(fl.readline())
        result = task(fl.readlines())

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write(str(result))

if __name__ == '__main__':
    main()
