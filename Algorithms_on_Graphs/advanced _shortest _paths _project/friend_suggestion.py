#!/usr/bin/python3

import sys
import heapq

class BiDijkstra:
    """
    A class to represent a bidirectional Dijkstra algorithm.

    ...

    Attributes
    ----------
    adj_list : list()
        Vertices and their neighbors
    weight : list()
        Weight of each edge
    adj_list_r : list()
        Vertices and their neighbors in the reverted graph
    weight_r : list()
        Weight of each edge in the reverted graph
    count : int()
        Counter for the number of queries made
    dist : dict()
        Vertices and their distance to the starting point
    dist_r : dict()
        Vertices and their distance to the arrival point in the reverted graph
    visited : dict()
        Visited vertices in both graphs
    heap : list()
        Min heap to process the vertex with the smallest distance
    heap_r : list()
        Minimum heap to process the vertex with the smallest distance in the reverted graph

    Methods
    -------
    reset(self):
        Clear the data structures for the following query.
    relax(self, vertex):
        Relaxes (sets the correct distance) of the neighbors of the given vertex
        and pushes them to the min heap so that they are relaxed later.
    relax_r(self, vertex):
        Relaxes (sets the correct distance) of the neighbors of the given vertex
        and pushes them to the min heap so that they are relaxed later, in the reverted graph.
    path(self):
        Modified road reconstruction function that only finds the minimum
        distance between the starting point and the destination.
    query(self, start_pt, end_pt):
        Given a starting and ending point, apply the bidirectional Dijkstra algorithm
        to find the minimum path distance between them, if there is such a path.

    """

    def __init__(self, adj_l, e_cost, adj_l_r, e_cost_r):
        """
        Constructs all the necessary attributes for a bidirectional Dijkstra algorithm:

        Parameters
        ----------
        adj_list : list()
            Vertices and their neighbors
        weight : list()
            Weight of each edge
        adj_list_r : list()
            Vertices and their neighbors in the reverted graph
        weight_r : list()
            Weight of each edge in the reverted graph
        count : int()
            Counter for the number of queries made
        dist : dict()
            Vertices and their distance to the starting point
        dist_r : dict()
            Vertices and their distance to the arrival point in the reverted graph
        visited : dict()
            Visited vertices in both graphs
        heap : list()
            Min heap to process the vertex with the smallest distance
        heap_r : list()
            Minimum heap to process the vertex with the smallest distance in the reverted graph
        """

        self.adj_list = adj_l
        self.weight = e_cost
        self.adj_list_r = adj_l_r
        self.weight_r = e_cost_r
        self.count = 0
        self.dist = dict()
        self.dist_r = dict()
        self.visited = dict()
        self.heap = list()
        self.heap_r = list()
        heapq.heapify(self.heap)
        heapq.heapify(self.heap_r)


    def reset(self):
        '''Clear the data structures for the following query.'''

        self.dist.clear()
        self.dist_r.clear()
        self.visited.clear()
        self.heap = list()
        self.heap_r = list()


    def relax(self, vertex):
        '''Relaxes (sets the correct distance) of the neighbors of the given vertex
        and pushes them to the min heap so that they are relaxed later.'''

        self.visited[vertex] = vertex

        w_neighbor = 0 # neighbor index to get the weight
        for neighbor in self.adj_list[vertex]:

            # float('inf') is used as the value in case the vertex is not in the dictionary yet.
            if self.dist.get(neighbor, float('inf')) > (self.dist.get(vertex) + self.weight[vertex][w_neighbor]):
                self.dist[neighbor] = (self.dist.get(vertex) + self.weight[vertex][w_neighbor])
                pair = [self.dist.get(neighbor), neighbor] # pair [distance, vertex]
                heapq.heappush(self.heap, pair)

            w_neighbor += 1


    def relax_r(self, vertex):
        '''Relaxes (sets the correct distance) of the neighbors of the given vertex
        and pushes them to the min heap so that they are relaxed later, in the reverted graph.'''

        self.visited[vertex] = vertex

        w_neighbor = 0 # neighbor index to get the weight
        for neighbor in self.adj_list_r[vertex]:

            # float('inf') is used as the value in case the vertex is not in the dictionary yet.
            if self.dist_r.get(neighbor, float('inf')) > (self.dist_r.get(vertex) + self.weight_r[vertex][w_neighbor]):
                self.dist_r[neighbor] = (self.dist_r.get(vertex) + self.weight_r[vertex][w_neighbor])
                pair = [self.dist_r.get(neighbor), neighbor] # pair [distance, vertex]
                heapq.heappush(self.heap_r, pair)

            w_neighbor += 1


    def path(self):
        '''Modified road reconstruction function that only finds the minimum
        distance between the starting point and the destination.'''

        distance = float('inf')

        for key, vertex in self.visited.items():
            if self.dist.get(vertex, float('inf')) + self.dist_r.get(vertex, float('inf')) < distance:
                distance = (self.dist.get(vertex) + self.dist_r.get(vertex))

        if distance == float('inf'):
            return -1 # there is no path
        return distance


    def query(self, start_pt, end_pt):
        '''Given a starting and ending point, apply the bidirectional Dijkstra algorithm
        to find the minimum path distance between them, if there is such a path.'''

        if self.count > 0:
            self.reset()

        if start_pt == end_pt:
            return 0

        self.dist[start_pt] = 0
        self.dist_r[end_pt] = 0

        pair = [self.dist.get(start_pt), start_pt] # pair [distance, vertex]
        pair_r = [self.dist_r.get(end_pt), end_pt] # pair [distance, vertex]
        heapq.heappush(self.heap, pair)
        heapq.heappush(self.heap_r, pair_r)


        while self.heap and self.heap_r:
            # Search in the original graph.
            min_vertex = heapq.heappop(self.heap)
            vertex = min_vertex[1]
            if vertex in self.visited: # there is a common vertex
                self.count += 1
                result = self.path()
                return result
            self.relax(vertex)

            # Search in the reverted graph.
            min_vertex = heapq.heappop(self.heap_r)
            vertex = min_vertex[1]
            if vertex in self.visited: # there is a common vertex
                self.count += 1
                result = self.path()
                return result
            self.relax_r(vertex)

        self.count += 1
        return -1 # there is no common vertex, there is no path


if __name__ == '__main__':
    graph = sys.stdin.read()
    data = list(map(int, graph.split()))
    n_ver, n_edg = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * n_edg):3], data[1:(3 * n_edg):3]), data[2:(3 * n_edg):3]))
    adj = [[] for _ in range(n_ver)]
    cost = [[] for _ in range(n_ver)]
    adj_r = [[] for _ in range(n_ver)]
    cost_r = [[] for _ in range(n_ver)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
        adj_r[b - 1].append(a - 1)
        cost_r[b - 1].append(w)
    bi = BiDijkstra(adj, cost, adj_r, cost_r)
    data = data[3 * n_edg:]
    data = data[1:]
    queries = [data[x:x+2] for x in range(0, len(data), 2)]
    for item in queries:
        start, end = item[0], item[1]
        print(bi.query(start - 1, end - 1))
