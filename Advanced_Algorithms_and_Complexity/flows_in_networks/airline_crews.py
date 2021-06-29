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
    A class to represent a bipartite graph.

    ...

    Attributes
    ----------
    num_v : int()
        Number of vertices in the graph
    num_flight : int()
        Number of flights
    matches : list()
        List that indicates whether the flight identified with the index number was matched
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
    find_match(self):
        Goes through the flights (left side of the graph) and see if they were matched and if so with which crew (right side of the graph).
    max_flow(self, start_pt, end_pt):
        Adds flow to the network until it is no longer possible, returns the maximum flow.

    """

    def __init__(self, n_ver, n_flights):
        self.num_v = n_ver
        self.num_flight = n_flights
        self.matches = [-1] * n_flights
        self.edges = []
        self.graph = [[] for _ in range(self.num_v)]

    def add_edge(self, from_, to_):
        '''Creates the graph adding an edge and its counterpart at the same time'''

        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to_, 1)
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

        min_cap = 1
        # remove excess edges
        path_edges = path_edges[:len(path)]

        return path, path_edges, min_cap

    def find_match(self):
        '''Goes through the flights (left side of the graph) and see if they were matched
        and if so with which crew (right side of the graph)'''

        for vertex in range(1, self.num_flight + 1):
            for id_edge in self.graph[vertex]:
                if id_edge % 2 != 0:
                    continue
                if self.edges[id_edge].capacity <= 0:
                    flight = self.edges[id_edge].n_start - 1
                    crew = self.edges[id_edge].n_end - self.num_flight
                    self.matches[flight] = crew
                    break

    def max_flow(self, start_pt, end_pt):
        '''Adds flow to the network until it is no longer possible, returns the matches in the bipartite graph.'''

        while True:

            path, path_edges, min_cap = self.get_path(start_pt, end_pt)

            if path == -1:
                self.find_match()
                return self.matches

            for id_edge in path_edges: # update edges capability
                self.add_flow(id_edge, min_cap)


def solve(n_flight, n_crew, edge_list):
    '''This function creates a bipartite graph'''

    vertex_count = n_flight + n_crew + 2
    graph = FlowGraph(vertex_count, n_flight)

    # create the edges from source to each flight vertex
    for i in range(n_flight):
        graph.add_edge(0, i + 1)

    # create the edges from the flight vertices to their possible crews
    for u_vertex, item in enumerate(edge_list):
        crew_vertex = n_flight

        for value in item:
            if value == 1:
                graph.add_edge(u_vertex + 1, crew_vertex + 1)

            crew_vertex += 1

    # create the edges from each vertex crew to end
    for i in range(n_flight + 1, vertex_count - 1):
        graph.add_edge(i, vertex_count - 1)

    result = graph.max_flow(0, graph.size() - 1)

    return result


if __name__ == '__main__':
    user = sys.stdin.read()
    data = list(map(int, user.split()))
    flights, crews = data[0:2]
    data = data[2:]
    edges = [data[x:x+crews] for x in range(0, len(data), crews)]
    list_matches = solve(flights, crews, edges)
    print(*list_matches)
