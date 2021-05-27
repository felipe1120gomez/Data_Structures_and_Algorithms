#!/usr/bin/python3

import sys
import heapq

class AStar:
    """
    A class to represent an A* algorithm.

    ...

    Attributes
    ----------
    adj_list : list()
        Vertices and their neighbors
    weight : list()
        Weight of each edge
    vertices : list()
        Vertices and their coordinates on the x and y axes
    count : int()
        Counter for the number of queries made
    dist : dict()
        Vertices and their distance to the starting point
    visited : dict()
        Visited vertices in the graph
    heap : list()
        Min heap to process the vertex with the lowest rank

    Methods
    -------
    reset(self):
        Clear the data structures for the following query.
    relax(self, vertex):
        Relaxes (sets the correct distance) of the neighbors of the given vertex
        and pushes them to the min heap so that they are relaxed later.
    query(self, start_pt, end_pt):
        Given a starting and ending point, apply the A* algorithm to find the
        minimum path distance between them, if there is such a path.

    """

    def __init__(self, adj_l, e_cost, vertices):
        """
        Constructs all the necessary attributes for an A* algorithm:

        Parameters
        ----------
        adj_list : list()
            Vertices and their neighbors
        weight : list()
            Weight of each edge
        vertices : list()
            Vertices and their coordinates on the x and y axes
        count : int()
            Counter for the number of queries made
        dist : dict()
            Vertices and their distance to the starting point
        visited : dict()
            Visited vertices in the graph
        heap : list()
            Min heap to process the vertex with the lowest rank
        """

        self.adj_list = adj_l
        self.weight = e_cost
        self.vertices = vertices
        self.count = 0
        self.dist = dict()
        self.visited = dict()
        self.heap = list()
        heapq.heapify(self.heap)


    def reset(self):
        '''Clear the data structures for the following query.'''

        self.dist.clear()
        self.visited.clear()
        self.heap = list()


    def relax(self, vertex, end_pt):
        '''Relaxes (sets the correct distance) of the neighbors of the given vertex
        and pushes them to the min heap so that they are relaxed later.
        Uses heuristic rank with a potential function for it.'''

        self.visited[vertex] = vertex
        e_x = self.vertices[end_pt][0] # x-axis coordinates
        e_y = self.vertices[end_pt][1] # y-axis coordinates

        w_neighbor = 0 # neighbor index to get the weight
        for neighbor in self.adj_list[vertex]:
            if neighbor in self.visited: # do not relax an already visited vertex
                w_neighbor += 1
                continue

            n_x = self.vertices[neighbor][0]
            n_y = self.vertices[neighbor][1]

            # float('inf') is used as the value in case the vertex is not in the dictionary yet.
            if self.dist.get(neighbor, float('inf')) > (self.dist.get(vertex) + self.weight[vertex][w_neighbor]):
                self.dist[neighbor] = (self.dist.get(vertex) + self.weight[vertex][w_neighbor])
                # potential function = distance from current vertex to end
                length = ((n_x - e_x)**2 + (n_y - e_y)**2)**0.5
                rank = self.dist.get(neighbor) + length
                pair = [rank, neighbor] # pair [rank, vertex]
                heapq.heappush(self.heap, pair)

            w_neighbor += 1


    def query(self, start_pt, end_pt):
        '''Given a starting and ending point, apply the A* algorithm to find the
        minimum path distance between them, if there is such a path.'''

        if self.count > 0:
            self.reset()

        if start_pt == end_pt:
            return 0

        self.dist[start_pt] = 0

        pair = [self.dist.get(start_pt), start_pt] # pair [distance, vertex]
        heapq.heappush(self.heap, pair)

        while self.heap:
            min_vertex = heapq.heappop(self.heap) # vertex with lowest rank
            vertex = min_vertex[1]
            if vertex == end_pt:
                break
            self.relax(vertex, end_pt)

        self.count += 1
        result = self.dist.get(end_pt, float('inf'))
        if result == float('inf'):
            return -1 # there is no path
        return result


if __name__ == '__main__':
    graph = sys.stdin.read()
    data = list(map(int, graph.split()))
    n_ver, n_edg = data[0:2]
    data = data[2:]
    x = data[0:2 * n_ver:2]
    y = data[1:2 * n_ver:2]
    points = list()
    for i in range(n_ver):
        point = [x[i], y[i]]
        points.append(point)
    data = data[2 * n_ver:]
    edges = list(zip(zip(data[0:(3 * n_edg):3], data[1:(3 * n_edg):3]), data[2:(3 * n_edg):3]))
    adj = [[] for _ in range(n_ver)]
    cost = [[] for _ in range(n_ver)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    path = AStar(adj, cost, points)
    data = data[3 * n_edg:]
    data = data[1:]
    queries = [data[x:x+2] for x in range(0, len(data), 2)]
    for item in queries:
        start, end = item[0], item[1]
        print(path.query(start - 1, end - 1))
