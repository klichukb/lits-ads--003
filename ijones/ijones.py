from collections import defaultdict
from string import ascii_lowercase

INFILE = 'ijones.in'
OUTFILE = 'ijones.out'


def solve(matrix, m, n, targets):
    # Solves using I.Jones dynamic programming.
    #
    # for j in N..1:
    # for i in 1..M:
    #   S[i][j] = {
    #       S[i][j + 1] + P[i + 1][M[i][j]],  M[i][j] != M[j][j + 1]
    #       P[i + 1][M[i][j]],                M[i][j] == M[j][j + 1]
    #   }
    #
    # P[i] is a map of characters and possible path counts that Mr. Jones can take if he happens
    # to be on the same character on any column on the left of [i].
    solutions = [0 for i in xrange(m)]
    path_count = dict.fromkeys(ascii_lowercase, 0)

    for i in targets:
        solutions[i] = 1
        path_count[matrix[i][n - 1]] += 1

    interested = {matrix[target][n - 1] for target in targets}
    for j in xrange(n - 2, -1, -1):
        # build updates here, apply later.
        defer = defaultdict(int)
        for i in xrange(m):
            cell = matrix[i][j]
            if cell not in interested:
                if not solutions[i]:
                    continue
            if cell == matrix[i][j + 1] or not solutions[i]:
                solution = path_count[cell]
            else:
                solution = solutions[i] + path_count[cell]
            solutions[i] = solution
            defer[cell] += solution
        # apply deferred updates
        for i, value in defer.items():
            interested.add(i)
            path_count[i] += value

    return sum(solutions)



def main():
    # read
    with open(INFILE, 'r') as fl:
        n, m = [int(token) for token in fl.readline().split()]
        matrix = fl.readlines()

    targets = (0, m - 1)
    # NOTE: stripping '\n' in lines relies only on value of `m` passed to solve().
    result = solve(matrix, m, n, targets)

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write(str(result))


if __name__ == '__main__':
    main()
