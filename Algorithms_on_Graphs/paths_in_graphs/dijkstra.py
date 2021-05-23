#Uses python3

import sys
import heapq

class Travel:
    """
    A class to represent a travel.

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
    end_pt : int()
        Arrival point of the travel
    prev : list()
        Vertices and its previous vertex, will be used to reconstruc the path
    dist : list()
        Vertices and their distance to the starting point

    Methods
    -------
    flight(self):
        Dijkstra algorithm, uses a min heap to explore the vertices with the shortest distance.
    distance(self):
        Reconstruct the path and determine if it is possible to connect
        the starting point and the arrival point.

    """

    def __init__(self, adj_l, e_cost, n_vr, s_pt, e_pt):
        """
        Constructs all the necessary attributes for a travel:

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
        end_pt : int()
            Arrival point of the travel
        prev : list()
            Vertices and its previous vertex, will be used to reconstruc the path
        dist : list()
            Vertices and their distance to the starting point
        """

        self.adj_list = adj_l
        self.weight = e_cost
        self.num_v = n_vr
        self.start_pt = s_pt
        self.end_pt = e_pt
        self.prev = [None for _ in range(self.num_v)]
        self.dist = [float('inf') for _ in range(self.num_v)] # infinite distance if not explored

    def flight(self):
        '''It travels the shortest path in a graph from the origin to the destination.'''

        self.dist[self.start_pt] = 0
        min_heap = list()
        heapq.heapify(min_heap)
        pair = [self.dist[self.start_pt], self.start_pt] # pair [distance, vertex]
        heapq.heappush(min_heap, pair)

        while min_heap:
            min_vertex = heapq.heappop(min_heap) # the pair with the shortest distance
            vertex = min_vertex[1]

            w_neighbor = 0 # neighbor index to get the weight
            for neighbor in self.adj_list[vertex]:
                if self.dist[neighbor] > (self.dist[vertex] + self.weight[vertex][w_neighbor]):
                    self.dist[neighbor] = (self.dist[vertex] + self.weight[vertex][w_neighbor])
                    self.prev[neighbor] = vertex
                    pair = [self.dist[neighbor], neighbor] # pair [distance, vertex]
                    heapq.heappush(min_heap, pair)

                w_neighbor += 1

    def distance(self):
        '''Reconstruct the path and determine if it is possible to connect the starting
        point and the arrival point. Returns the cost of the shortest cost path.'''

        self.flight()

        result = list()

        point = self.end_pt # we go from end to start

        while point != self.start_pt: # path reconstruction
            result.append(point)
            point = self.prev[point]
            if point is None:
                return -1 # there is no path from start to end

        return self.dist[self.end_pt]


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
    start, end = data[0] - 1, data[1] - 1
    travel = Travel(adj, cost, n_ver, start, end)
    print(travel.distance())
