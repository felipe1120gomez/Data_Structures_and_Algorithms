#Uses python3

import sys
from collections import deque

class Travel:
    """
    A class to represent a travel.

    ...

    Attributes
    ----------
    adj_list : list()
        Vertices and their neighbors
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
    process : deque()
        Queue to explore vertices in the order they are discovered

    Methods
    -------
    bfs(self):
        Breadth first search, explores all neighboring vertices to the starting point.
    distance(self):
        Reconstruct the path and determine if it is possible to connect
        the starting point and the arrival point.

    """

    def __init__(self, adj_l, n_vr, s_pt, e_pt):
        """
        Constructs all the necessary attributes for a travel:

        Parameters
        ----------
        adj_list : list()
            Vertices and their neighbors
        num_v : int()
            Number of vertices
        start_pt : int()
            Starting point of the travel
        end_pt : int()
            Arrival point of the travel
        prev : list()
            Vertices and its previous vertex, will be used to rebuild the path
        dist : list()
            Vertices and their distance to the starting point
        process : deque()
            Queue to explore vertices in the order they are discovered
        """

        self.adj_list = adj_l
        self.num_v = n_vr
        self.start_pt = s_pt
        self.end_pt = e_pt
        self.prev = [None for _ in range(self.num_v)]
        self.dist = [None for _ in range(self.num_v)]
        self.process = deque()

    def bfs(self):
        '''Breadth first search, explores all neighboring vertices to the starting point.'''

        # we only discover the vertices connected to star, if end is not one of them
        # we will never find out, this algorithm does not traverse isolated vertices
        self.dist[self.start_pt] = 0
        self.process.append(self.start_pt)

        while self.process:
            vertex = self.process.popleft()

            for neighbor in self.adj_list[vertex]:
                if self.dist[neighbor] is None: # if it has not been explored
                    self.process.append(neighbor)
                    self.dist[neighbor] = self.dist[vertex] + 1
                    self.prev[neighbor] = vertex

    def distance(self):
        '''Reconstruct the path and determine if it is possible to connect
        the starting point and the arrival point. Returns the distance if there is a path.'''

        self.bfs()

        path = list()

        point = self.end_pt # we go from end to start

        while point != self.start_pt: # path reconstruction
            path.append(point)
            point = self.prev[point]
            if point is None:
                return -1 # there is no path from start to end

        return len(path)

if __name__ == '__main__':
    graph = sys.stdin.read()
    data = list(map(int, graph.split()))
    n_ver, n_edg = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * n_edg):2], data[1:(2 * n_edg):2]))
    adj = [[] for _ in range(n_ver)] # list of vertices and their neighbors
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    start, end = data[2 * n_edg] - 1, data[2 * n_edg + 1] - 1
    travel = Travel(adj, n_ver, start, end)
    print(travel.distance())
