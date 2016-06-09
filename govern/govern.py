import sys

INFILE = 'govern.in'
OUTFILE = 'govern.out'

VISITED = 1
RESOLVED = 2


class Vertex(object):
    def __init__(self, name, out_edges=None):
        self.name = name
        self.out_edges = out_edges or []

    def __repr__(self):
        return self.name


class Edge(object):
    def __init__(self, start_v, end_v):
        self.start_v = start_v
        self.end_v = end_v

    def __repr__(self):
        return u'{} -> {}'.format(self.start_v, self.end_v)


class Graph(object):
    def __init__(self, vertices=None):
        self.vertices = vertices or {}


def dfs(graph):
    unvisited = set(graph.vertices.values())
    status = {}
    order_set = set()

    while unvisited:
        for vertex in dfs_iteration(status, unvisited, unvisited.pop()):
            if vertex in order_set:
                continue
            order_set.add(vertex)
            yield vertex


def dfs_iteration(status, unvisited, start_v):
    stack = [start_v]
    while stack:
        vertex = stack.pop()
        if vertex in unvisited:
            unvisited.remove(vertex)

        if status.get(vertex.name) == RESOLVED:
            continue

        neighbors = [edge.end_v for edge in vertex.out_edges if edge.end_v.name not in status]
        if neighbors:
            status[vertex.name] = VISITED
            stack.append(vertex)
            stack.extend(neighbors)
        else:
            status[vertex.name] = RESOLVED
            yield vertex


def get_topological_sort(graph):
    return dfs(graph)


def read_graph(fl):
    graph = Graph()
    for line in fl.readlines():
        _from, to = line.rstrip().split()

        # get or create start v
        start_v = graph.vertices.get(_from)
        if not start_v:
            start_v = graph.vertices[_from] = Vertex(_from, [])
        # get or create end v
        end_v = graph.vertices.get(to)
        if not end_v:
            end_v = graph.vertices[to] = Vertex(to, [])

        start_v.out_edges.append(Edge(start_v, end_v))
    return graph


def main():
    # read
    with open(sys.argv[1] if len(sys.argv) > 1 else INFILE, 'r') as fl:
        graph = read_graph(fl)
        path = get_topological_sort(graph)

    # yes, all in memory. but only one I/O call on write(), right?
    result = '\n'.join(str(line) for line in path) + '\n'

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write(result)

if __name__ == '__main__':
    main()
