# python3

import sys
from collections import deque

class Edge:
    """
    A class to represent an edge in the graph.

    ...

    Attributes
    ----------
    n_start : Edge instance
        Vertex where the edge starts
    n_end : Edge instance
        Vertex where the edge ends
    capacity : Edge instance
        Amount of flow that can pass over the edge

    Methods
    -------

    """

    def __init__(self, n_s, n_e, capacity):
        self.n_start = n_s
        self.n_end = n_e
        self.capacity = capacity

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:
    """
    A class to represent a network.

    ...

    Attributes
    ----------
    num_v : int()
        Number of vertices in the graph
    edges : list()
        List of all - forward and backward - edges
    graph : 2D array()
        These adjacency lists store only indices of edges in the edges list

    Methods
    -------
    add_edge(self, from_, to_, capacity):
        Creates the graph adding an edge and its counterpart at the same time.
    size(self):
        Returns the size of the graph.
    add_flow(self, id_edge, flow):
        Adds flow to the edge by decreasing its capacity and increasing its counterpart.
    bfs(self, start_pt, end_pt):
        Breadth first search.
    get_path(self, start_pt, end_pt):
        Reconstructs the path and determine if it is possible to connect the starting point and the end point.
    max_flow(self, start_pt, end_pt):
        Adds flow to the network until it is no longer possible, returns the maximum flow.

    """

    def __init__(self, n_ver):
        self.num_v = n_ver
        self.edges = []
        self.graph = [[] for _ in range(self.num_v)]

    def add_edge(self, from_, to_, capacity):
        '''Creates the graph adding an edge and its counterpart at the same time'''

        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to_, capacity)
        backward_edge = Edge(to_, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        # Residual network of opposite edges
        self.graph[to_].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        '''Returns the size of the graph'''

        return len(self.graph)

    def add_flow(self, id_edge, flow):
        '''Adds flow to the edge by decreasing its capacity and increasing its counterpart'''

        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        # when we go through an edge its capacity decreases
        # but that of its inverted edge increases
        # this allows us to use this inverted edge in case there is no path
        self.edges[id_edge].capacity -= flow
        self.edges[id_edge ^ 1].capacity += flow

    def bfs(self, start_pt, end_pt):
        '''Breadth first search'''

        prev = [None for _ in range(self.num_v)]
        dist = [None for _ in range(self.num_v)]
        path_edges = list() # edges visited when trying to find a path
        process = deque()
        dist[start_pt] = 0
        process.append(start_pt)

        while process:
            vertex = process.popleft()

            # we try to find a way in both networks
            for id_edge in self.graph[vertex]:

                neighbor = self.edges[id_edge].n_end

                if dist[neighbor] is None and self.edges[id_edge].capacity > 0:
                    path_edges.append(id_edge)
                    process.append(neighbor)
                    dist[neighbor] = dist[vertex] + 1
                    prev[neighbor] = vertex
                    if neighbor == end_pt: # path found
                        return prev, path_edges


        return prev, path_edges

    def get_path(self, start_pt, end_pt):
        '''Reconstructs the path and determine if it is possible to connect
        the starting point and the end point. Returns the path,
        indices in the edges list() and the minimum capacity if there is a path.'''

        prev, path_edges = self.bfs(start_pt, end_pt)

        path = list()

        point = end_pt # we go from end to start

        while point != start_pt: # path reconstruction
            path.append(point)
            point = prev[point]
            if point is None:
                return -1, path_edges, 0 # there is no path from start to end

        path = path[::-1]
        capacities = list()
        vertex = 0
        index = 0
        len_edges = len(path_edges)

        # leave only the edges that correspond to the vertices in the path.
        for _ in range(len_edges):
            edge = path_edges[index]

            if self.edges[edge].n_end == path[vertex]:
                capacities.append(self.edges[edge].capacity)
                vertex += 1
                index += 1
                if len(capacities) == len(path):
                    break

            else:
                path_edges.pop(index)

        min_cap = min(capacities)
        # remove excess edges
        path_edges = path_edges[:len(path)]

        return path, path_edges, min_cap


    def max_flow(self, start_pt, end_pt):
        '''Adds flow to the network until it is no longer possible, returns the maximum flow'''

        flow = 0

        while True:

            path, path_edges, min_cap = self.get_path(start_pt, end_pt)

            if path == -1:
                return flow

            for id_edge in path_edges: # update edges capability
                self.add_flow(id_edge, min_cap)

            flow += min_cap


if __name__ == '__main__':
    user = sys.stdin.read()
    data = list(map(int, user.split()))
    vertex_count, edge_count = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(3 * edge_count):3], data[1:(3 * edge_count):3], data[2:(3 * edge_count):3]))
    graph = FlowGraph(vertex_count)
    for i in range(edge_count):
        node_s, node_e, cap = edges[i]
        graph.add_edge(node_s - 1, node_e - 1, cap)

    print(graph.max_flow(0, graph.size() - 1))
