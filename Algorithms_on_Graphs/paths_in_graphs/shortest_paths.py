#Uses python3

import sys
from collections import deque

class Paths:
    """
    A class to represent a path finder in a graph.

    ...

    Attributes
    ----------
    adj_list : list()
        Vertices and their neighbors
    weight : list()
        Weight of each edge
    num_v : int()
        Number of vertices
    start_pt : int()
        Starting point of the travel
    prev : list()
        Vertices and its previous vertex, will be used to reconstruc the path
    reach : list()
        Boolean list that determines which vertices can be reached from the start
    inf : list()
        Boolean list that determines which vertices belong to an infinite arbitrage
    dist : list()
        Vertices and their distance to the starting point
    last_relax : list()
        Vertices that belong to an infinite arbitrage
    visited : dict()
        Visited vertices

    Methods
    -------
    bellman_ford(self):
        Modified Bellman Ford algorithm to check if there is a cycle of negative weight in the graph.
    bf_search(self, ver):
        Breadth first search, explores all neighboring vertices to the give vertex,
        this vertex and its neighbors are part of an infinite arbitrage.
    infinte_arbitrage(self):
        Traverse all vertices of an infinite arbitrage, and call
        the bf_search function with each vertex not traversed.
    distance(self):
        Reconstruct the path and determine if it is possible to connect
        the starting point and the other vertices.
    shortet_paths(self):
        Call the other functions according to the characteristics of the graph.

    """

    def __init__(self, adj_l, e_cost, s_pt, n_vr):
        """
        Constructs all the necessary attributes for a path finder in a graph:

        Parameters
        ----------
        adj_list : list()
            Vertices and their neighbors
        weight : list()
            Weight of each edge
        num_v : int()
            Number of vertices
        start_pt : int()
            Starting point of the travel
        prev : list()
            Vertices and its previous vertex, will be used to reconstruc the path
        reach : list()
            Boolean list that determines which vertices can be reached from the start
        inf : list()
            Boolean list that determines which vertices belong to an infinite arbitrage
        dist : list()
            Vertices and their distance to the starting point
        last_relax : list()
            Vertices that belong to an infinite arbitrage
        visited : dict()
            Visited vertices
        """

        self.adj_list = adj_l
        self.weight = e_cost
        self.num_v = n_vr
        self.start_pt = s_pt
        self.prev = [None for _ in range(self.num_v)]
        self.reach = [True for _ in range(self.num_v)]
        self.inf = [False for _ in range(self.num_v)]
        self.dist = [float('inf') for _ in range(self.num_v)]
        self.last_relax = list()
        self.visited = dict()

    def bellman_ford(self):
        '''Modified Bellman Ford algorithm to find cycles of negative weight in a graph
        and select the vertices that belong to an infinite arbitrage.'''

        self.dist[self.start_pt] = 0

        for i in range(1, self.num_v + 1): # num_v iterations

            for vertex in range(self.num_v):

                for neighbor in self.adj_list[vertex]:
                    w_neighbor = self.adj_list[vertex].index(neighbor) # neighbor index to check the weight
                    if self.dist[neighbor] > (self.dist[vertex] + self.weight[vertex][w_neighbor]):
                        self.dist[neighbor] = (self.dist[vertex] + self.weight[vertex][w_neighbor])
                        self.prev[neighbor] = vertex
                        # if iteration num_v modifies any distance, there is a negative cycle
                        if i == (self.num_v):
                            self.last_relax.append(neighbor) # this neighbor belongs to an infinite arbitrage

    def bf_search(self, ver):
        '''Breadth first search, explores all neighboring vertices to the give vertex,
        this vertex and its neighbors are part of an infinite arbitrage.'''

        process = deque()
        process.append(ver)

        while process:
            vertex = process.popleft()

            if vertex not in self.visited:
                self.inf[vertex] = True
                # change the value to True to indicate that it belongs to an infinite arbitrage

            self.visited[vertex] = 'visited'

            for neighbor in self.adj_list[vertex]:
                if neighbor not in self.visited:
                    self.inf[neighbor] = True
                    process.append(neighbor)


    def infinte_arbitrage(self):
        '''Traverse all vertices of an infinite arbitrage, and call
        the bf_search function with each vertex not traversed.'''

        for vertex in self.last_relax: # vertex = index in the list
            if vertex not in self.visited:
                self.bf_search(vertex)


    def distance(self):
        '''Reconstruct the path and determine if it is possible to connect
        the starting point and the other vertices.'''

        for end in range(self.num_v): # reconstruct the path for all vertices of the graph

            if self.inf[end]: # if the vertex belongs to an infinite arbitrage, skip it
                continue

            point = end # we go from end to start

            while point != self.start_pt: # path reconstruction
                point = self.prev[point]
                if point is None:
                    self.reach[end] = False # there is no path from start to end
                    break


    def shortet_paths(self):
        '''Call the other functions according to the characteristics of the graph.'''

        self.bellman_ford()

        cycle = len(self.last_relax)
        # if there is at least one vertex in the list, there is infinite arbitrage

        if cycle:
            self.infinte_arbitrage()

        self.distance()
        # there is no infinite arbitrage, only determine the vertices
        # that can be reached from the start

        return self.reach, self.inf, self.dist


if __name__ == '__main__':
    graph = sys.stdin.read()
    data = list(map(int, graph.split()))
    n_ver, n_edg = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * n_edg):3], data[1:(3 * n_edg):3]), data[2:(3 * n_edg):3]))
    data = data[3 * n_edg:]
    adj = [[] for _ in range(n_ver)] # list of vertices and their neighbors
    cost = [[] for _ in range(n_ver)] # list of vertices and their weights
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    start = data[0] - 1
    path = Paths(adj, cost, start, n_ver)
    reachable, infinite, distance = path.shortet_paths()
    for x in range(n_ver):
        if not reachable[x]: # vertex not reachable
            print('*')
        elif infinite[x]: # reachable vertex but in infinite arbitrage
            print('-')
        else:
            print(distance[x])
