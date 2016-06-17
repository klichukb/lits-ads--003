import sys

INFILE = 'wchain.in'
OUTFILE = 'wchain.out'


def get_max_path_lengths(words):
    """
    Get local max path lengths for chains, found in `words`.
    """
    # Uses dynamic programming approach.
    #
    # Recurrent behavior:
    #     S[word] = max(S[child] for child in all_children(word)) + 1
    #
    # Solutions should grow from shorter words to longer, so that any complex word should
    # be able to reach longest path lengths calculated for possible direct children, if any.
    words.sort(key=len)
    solutions = {}
    solutions[words[0]] = 1
    for parent in words[1:]:
        max_length = 0
        for i in xrange(len(parent)):
            option = parent[:i] + parent[i + 1:]
            if option not in solutions:
                continue
            option_length = solutions[option]
            if option_length > max_length:
                max_length = option_length
        max_length += 1
        solutions[parent] = max_length
        yield max_length


def solve(words):
    return max(get_max_path_lengths(words))


def main():
    # read
    with open(sys.argv[1] if len(sys.argv) > 1 else INFILE, 'r') as fl:
        fl.readline()
        words = [ln.strip() for ln in fl.readlines()]

    result = solve(words)

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write(str(result))


if __name__ == '__main__':
    main()
