#Uses python3

import sys
import heapq

class Paths:
    """
    A class to represent a minimum spanning tree.

    ...

    Attributes
    ----------
    vertices : list()
        Vertices and their coordinates on the x and y axes
    num_v : int()
        Number of vertices
    dist : list()
        Vertices and their distance to the starting point
    visited : dict()
        Visited vertices

    Methods
    -------
    prim(self):
        Prim algorithm to create a minimal spanning tree.

    """

    def __init__(self, vertices, n_vr):
        """
        Constructs all the necessary attributes for a minimum spanning tree:

        Parameters
        ----------
        vertices : list()
            Vertices and their coordinates on the x and y axes
        num_v : int()
            Number of vertices
        dist : list()
            Vertices and their distance to the starting point
        visited : dict()
            Visited vertices
        """

        self.vertices = vertices
        self.num_v = n_vr
        self.dist = [float('inf') for _ in range(self.num_v)]
        self.visited = dict()

    def prim(self):
        '''Prim algorithm to create a minimal spanning tree
        Returns the total cost of the tree.'''

        root = 0 # starting point
        self.dist[root] = 0
        min_heap = list()
        heapq.heapify(min_heap)
        cost = [self.dist[root], root] # pair [distance, vertex]
        heapq.heappush(min_heap, cost)

        while min_heap:
            min_vertex = heapq.heappop(min_heap) # the pair with the shortest distance
            vertex = min_vertex[1]
            self.visited[vertex] = 'visited'
            v_x = self.vertices[vertex][0] # x-axis coordinates
            v_y = self.vertices[vertex][1] # y-axis coordinates

            for neighbor in range(self.num_v):
                n_x = self.vertices[neighbor][0]
                n_y = self.vertices[neighbor][1]

                # the length of a segment with endpoints (𝑥1, 𝑦1) and (𝑥2, 𝑦2)
                # is equal to √︀(𝑥1 − 𝑥2)^2 + (𝑦1 − 𝑦2)^2.
                length = ((v_x - n_x)**2 + (v_y - n_y)**2)**0.5

                if neighbor not in self.visited and self.dist[neighbor] > length:
                    self.dist[neighbor] = length
                    cost = [self.dist[neighbor], neighbor]
                    heapq.heappush(min_heap, cost)

        return float(sum(self.dist))


if __name__ == '__main__':
    graph = sys.stdin.read()
    data = list(map(int, graph.split()))
    n_ver = data[0]
    x = data[1::2]
    y = data[2::2]
    points = list()
    for i in range(n_ver):
        point = [x[i], y[i]]
        points.append(point)
    path = Paths(points, n_ver)
    print("{0:.9f}".format(path.prim()))
