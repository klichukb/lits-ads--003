INFILE = 'bugtrk.in'
OUTFILE = 'bugtrk.out'


def task(N, W, H):
    max_a = max(W, H) * N
    left = 1
    right = max_a
    middle = 1
    while left < right:
        middle = (left + right) // 2
        curr_n = (middle // W) * (middle // H)
        if curr_n < N:
            left = middle + 1
        elif curr_n >= N:
            right = middle
        else:
            return middle
    return middle if right < left else left


def main():
    # read
    with open(INFILE, 'r') as fl:
        result = task(*(int(tok) for tok in fl.readline().split()))

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write(str(result))

if __name__ == '__main__':
    main()
