#!/usr/bin/python3

import sys
import heapq

class AStar:
    """
    A class to represent a bidirectional A* algorithm.

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
    vertices : list()
        Vertices and their coordinates on the x and y axes
    count : int()
        Counter for the number of queries made
    dist : dict()
        Vertices and their distance to the starting point
    dist_r : dict()
        Vertices and their distance to the arrival point in the reverted graph
    visited : dict()
        Visited vertices in both graphs
    proc : dict()
        Visited vertices in the original graph
    proc_r : dict()
        Visited vertices in the reverted graph
    heap : list()
        Min heap to process the vertex with the lowest rank
    heap_r : list()
        Minimum heap to process the vertex with the lowest rank in the reverted graph

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
        Given a starting and ending point, apply the bidirectional A* algorithm
        to find the minimum path distance between them, if there is such a path.

    """

    def __init__(self, adj_l, e_cost, adj_l_r, e_cost_r, vertices):
        """
        Constructs all the necessary attributes for a bidirectional A* algorithm:

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
        vertices : list()
            Vertices and their coordinates on the x and y axes
        count : int()
            Counter for the number of queries made
        dist : dict()
            Vertices and their distance to the starting point
        dist_r : dict()
            Vertices and their distance to the arrival point in the reverted graph
        visited : dict()
            Visited vertices in both graphs
        proc : dict()
            Visited vertices in the original graph
        proc_r : dict()
            Visited vertices in the reverted graph
        heap : list()
            Min heap to process the vertex with the lowest rank
        heap_r : list()
            Minimum heap to process the vertex with the lowest rank in the reverted graph
        """

        self.adj_list = adj_l
        self.weight = e_cost
        self.adj_list_r = adj_l_r
        self.weight_r = e_cost_r
        self.vertices = vertices
        self.count = 0
        self.dist = dict()
        self.dist_r = dict()
        self.visited = dict()
        self.proc = dict()
        self.proc_r = dict()
        self.heap = list()
        self.heap_r = list()
        heapq.heapify(self.heap)
        heapq.heapify(self.heap_r)


    def reset(self):
        '''Clear the data structures for the following query.'''

        self.dist.clear()
        self.dist_r.clear()
        self.visited.clear()
        self.proc.clear()
        self.proc_r.clear()
        self.heap = list()
        self.heap_r = list()


    def relax(self, vertex, start, end):
        '''Relaxes (sets the correct distance) of the neighbors of the given vertex
        and pushes them to the min heap so that they are relaxed later.
        Uses heuristic rank with the average of potential functions for it.'''

        self.visited[vertex] = vertex
        self.proc[vertex] = vertex
        # x-axis and y-axis coordinates
        s_x = self.vertices[start][0]
        s_y = self.vertices[start][1]
        e_x = self.vertices[end][0]
        e_y = self.vertices[end][1]

        w_neighbor = 0 # neighbor index to get the weight
        for neighbor in self.adj_list[vertex]:
            if neighbor in self.proc: # do not relax an already visited vertex
                w_neighbor += 1
                continue

            n_x = self.vertices[neighbor][0]
            n_y = self.vertices[neighbor][1]

            # float('inf') is used as the value in case the vertex is not in the dictionary yet.
            if self.dist.get(neighbor, float('inf')) > (self.dist.get(vertex) + self.weight[vertex][w_neighbor]):
                self.dist[neighbor] = (self.dist.get(vertex) + self.weight[vertex][w_neighbor])
                # potential function = distance from current vertex to end
                potential = ((n_x - e_x)**2 + (n_y - e_y)**2)**0.5
                # potential function = distance from start to current vertex
                potential_r = ((s_x - n_x)**2 + (s_y - n_y)**2)**0.5
                # average of potential functions
                average_pot = (potential - potential_r) / 2
                rank = self.dist.get(neighbor) + average_pot
                pair = [rank, neighbor] # pair [rank, vertex]
                heapq.heappush(self.heap, pair)

            w_neighbor += 1


    def relax_r(self, vertex, start, end):
        '''Relaxes (sets the correct distance) of the neighbors of the given vertex
        and pushes them to the min heap so that they are relaxed later.
        Uses heuristic rank with the average of potential functions for it, in the reverted graph.'''

        self.visited[vertex] = vertex
        self.proc_r[vertex] = vertex
        # x-axis and y-axis coordinates
        s_x = self.vertices[start][0]
        s_y = self.vertices[start][1]
        e_x = self.vertices[end][0]
        e_y = self.vertices[end][1]

        w_neighbor = 0 # neighbor index to get the weight
        for neighbor in self.adj_list_r[vertex]:
            if neighbor in self.proc_r: # do not relax an already visited vertex
                w_neighbor += 1
                continue
            n_x = self.vertices[neighbor][0]
            n_y = self.vertices[neighbor][1]

            # float('inf') is used as the value in case the vertex is not in the dictionary yet.
            if self.dist_r.get(neighbor, float('inf')) > (self.dist_r.get(vertex) + self.weight_r[vertex][w_neighbor]):
                self.dist_r[neighbor] = (self.dist_r.get(vertex) + self.weight_r[vertex][w_neighbor])
                # potential function = distance from current vertex to end
                potential = ((n_x - e_x)**2 + (n_y - e_y)**2)**0.5
                # potential function = distance from start to current vertex
                potential_r = ((s_x - n_x)**2 + (s_y - n_y)**2)**0.5
                # average of potential functions
                average_pot = (potential_r - potential) / 2
                rank = self.dist_r.get(neighbor) + average_pot
                pair = [rank, neighbor] # pair [rank, vertex]
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
        '''Given a starting and ending point, apply the bidirectional A* algorithm
        to find the minimum path distance between them, if there is such a path.'''

        if self.count > 0:
            self.reset()

        if start_pt == end_pt:
            return 0

        # x-axis and y-axis coordinates
        s_x = self.vertices[start_pt][0]
        s_y = self.vertices[start_pt][1]
        e_x = self.vertices[end_pt][0]
        e_y = self.vertices[end_pt][1]
        # potential function = distance from end to end
        potential = ((e_x - e_x)**2 + (e_y - e_y)**2)**0.5
        # potential function = distance from start to end
        potential_r = ((s_x - e_x)**2 + (s_y - e_y)**2)**0.5
        # average of potential functions
        average_pot = (potential_r - potential) / 2

        self.dist[start_pt] = 0
        self.dist_r[end_pt] = 0

        pair = [self.dist.get(start_pt), start_pt]
        pair_r = [self.dist_r.get(end_pt), end_pt]
        heapq.heappush(self.heap, pair)
        heapq.heappush(self.heap_r, pair_r)


        while self.heap and self.heap_r:
            min_vertex = heapq.heappop(self.heap)
            vertex = min_vertex[1]

            min_vertex = heapq.heappop(self.heap_r)
            vertex_r = min_vertex[1]

            top = self.dist.get(vertex, float('inf'))
            top_r = self.dist_r.get(vertex_r, float('inf'))
            best = self.dist.get(end_pt, float('inf')) # best distance to destination seen so far

            # stop condition
            if top + top_r >= best + average_pot:
                self.count += 1
                result = self.path()
                return result

            # Search in the original graph
            self.relax(vertex, start_pt, end_pt)
            # Search in the reverted graph.
            self.relax_r(vertex_r, start_pt, end_pt)


        self.count += 1
        result = self.path()
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
    adj_r = [[] for _ in range(n_ver)]
    cost_r = [[] for _ in range(n_ver)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
        adj_r[b - 1].append(a - 1)
        cost_r[b - 1].append(w)
    path = AStar(adj, cost, adj_r, cost_r, points)
    data = data[3 * n_edg:]
    data = data[1:]
    queries = [data[x:x+2] for x in range(0, len(data), 2)]
    for item in queries:
        start, end = item[0], item[1]
        print(path.query(start - 1, end - 1))
