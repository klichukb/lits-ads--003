import sys

INFILE = 'career.in'
OUTFILE = 'career.out'


def solve(points, max_levels):
    solutions = [0 for i in range(max_levels)]
    solutions[:max_levels] = points[-1]
    for i in xrange(max_levels - 1, -1, -1):
        for j in xrange(i):
            solutions[j] = max(solutions[j], solutions[j + 1]) + points[i - 1][j]
    return solutions[0]


def main():
    # read
    with open(sys.argv[1] if len(sys.argv) > 1 else INFILE, 'r') as fl:
        max_levels = int(fl.readline())
        points = [[int(num) for num in ln.split()] for ln in fl.readlines()]

    result = solve(points, max_levels)

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write(str(result))


if __name__ == '__main__':
    main()
