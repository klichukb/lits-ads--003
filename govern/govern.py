import sys
from collections import defaultdict
from itertools import count

INFILE = 'govern.in'
OUTFILE = 'govern.out'

VISITED = 1
RESOLVED = 2


def dfs(graph):
    unvisited = set(graph.keys())
    status = {}
    order_set = set()

    while unvisited:
        for vertex in dfs_iteration(graph, status, unvisited, unvisited.pop()):
            if vertex in order_set:
                continue
            order_set.add(vertex)
            yield vertex


def dfs_iteration(graph, status, unvisited, start_v):
    stack = [start_v]
    while stack:
        vertex = stack.pop()
        if vertex in unvisited:
            unvisited.remove(vertex)

        if status.get(vertex) == RESOLVED:
            continue

        neighbors = [edge for edge in graph[vertex] if edge not in status]
        if neighbors:
            status[vertex] = VISITED
            stack.append(vertex)
            stack.extend(neighbors)
        else:
            status[vertex] = RESOLVED
            yield vertex


def get_topological_sort(graph):
    return dfs(graph)


def read_graph(fl):
    graph = defaultdict(set)
    mapping = {}
    rev_mapping = {}
    i = count()
    for line in fl.readlines():
        _from, to = line.rstrip().split()
        start_v = mapping.get(_from)
        if start_v is None:
            start_v = mapping[_from] = i.next()
            rev_mapping[start_v] = _from
        end_v = mapping.get(to)
        if end_v is None:
            end_v = mapping[to] = i.next()
            rev_mapping[end_v] = to
        graph[start_v].add(end_v)
    return rev_mapping, graph


def main():
    # read
    with open(sys.argv[1] if len(sys.argv) > 1 else INFILE, 'r') as fl:
        mapping, graph = read_graph(fl)
        path = get_topological_sort(graph)

    # yes, all in memory. but only one I/O call on write(), right?
    result = '\n'.join(mapping[line] for line in path) + '\n'

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write(result)

if __name__ == '__main__':
    main()
