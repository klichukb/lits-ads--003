import heapq
import sys

INFILE = 'gamsrv.in'
OUTFILE = 'gamsrv.out'

VISITED = 1
RESOLVED = 2


class Vertex(object):
    def __init__(self, index, out_edges=None):
        self.index = index
        self.out_edges = out_edges or []

    def __repr__(self):
        return 'V({})'.format(self.index)


class Edge(object):
    def __init__(self, start_v, end_v, weight):
        self.start_v = start_v
        self.end_v = end_v
        self.weight = weight

    def __repr__(self):
        return u'{} - [{}] - {}'.format(self.start_v, self.weight, self.end_v)


class Graph(object):
    def __init__(self, vertices=None, client_vertices=None):
        self.vertices = vertices or []
        self.client_vertices = client_vertices or set()


def read_graph(fl):
    vertex_count, edge_count = [int(tok) for tok in fl.readline().split()]
    vertices = [Vertex(i, []) for i in xrange(vertex_count)]
    client_vertices = {int(tok) - 1 for tok in fl.readline().split()}
    graph = Graph(vertices=vertices, client_vertices=client_vertices)

    for line in fl.readlines():
        _from, to, weight = [int(tok) for tok in line.rstrip().split()]
        _from -= 1
        to -= 1
        start_v = graph.vertices[_from]
        end_v = graph.vertices[to]
        start_v.out_edges.append(Edge(start_v, end_v, weight))
        end_v.out_edges.append(Edge(end_v, start_v, weight))
    return graph


def shortest_path_for(graph, start_v):
    # Dijkstra for a single vertex.
    distances = [float('inf')] * len(graph.vertices)
    distances[start_v.index] = 0
    pq = [(0, start_v)]
    while pq:
        distance, vertex = heapq.heappop(pq)
        for edge in vertex.out_edges:
            neighbor = edge.end_v
            new_distance = distance + edge.weight
            if new_distance < distances[neighbor.index]:
                distances[neighbor.index] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))
    return distances


def all_shortest_paths(graph):
    # Dijkstra for each eligible vertex (non-client).
    for vertex in graph.vertices:
        if vertex.index in graph.client_vertices:
            continue
        distances = shortest_path_for(graph, vertex)
        yield max(dst for v, dst in enumerate(distances) if v in graph.client_vertices)


def main():
    # read
    with open(sys.argv[1] if len(sys.argv) > 1 else INFILE, 'r') as fl:
        graph = read_graph(fl)
        result = min(all_shortest_paths(graph))

    # write
    with open(OUTFILE, 'w') as fl:
        fl.write(str(result))

if __name__ == '__main__':
    main()
