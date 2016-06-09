import sys

INFILE = 'govern.in'
OUTFILE = 'govern.out'


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

    def get_or_create_vertex(self, name):
        vertex = self.vertices.get(name)
        if not vertex:
            vertex = self.vertices[name] = Vertex(name, [])
        return vertex

    def __iter__(self):
        return self.vertices.iterkeys()

    def __getitem__(self, key):
        return self.get_or_create_vertex(key)

VISITED = 1
RESOLVED = 2


def get_topological_sort(graph):
    return dfs(graph)


def dfs(graph):
    unvisited = set(graph.vertices.values())
    status = {}
    order_set = set()

    while unvisited:
        for v in dfs_iteration(graph, status, unvisited, unvisited.pop()):
            if v not in order_set:
                order_set.add(v)
                yield v


def dfs_iteration(graph, status, unvisited, start_v):
    stack = [start_v]
    while (stack):
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


def read_graph(fl):
    graph = Graph()
    for line in fl.readlines():
        _from, to = line.rstrip().split()
        start_v, end_v = graph[_from], graph[to]
        start_v.out_edges.append(Edge(start_v, end_v))
    return graph


def main():

    # read
    with open(sys.argv[1] if len(sys.argv) > 1 else INFILE, 'r') as fl:
        graph = read_graph(fl)
        path = get_topological_sort(graph)

    result = '\n'.join(str(line) for line in path) + '\n'

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write(result)

if __name__ == '__main__':
    main()
