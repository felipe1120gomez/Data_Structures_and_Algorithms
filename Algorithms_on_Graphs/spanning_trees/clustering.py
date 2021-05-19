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
    num_clus : int()
        Number if clusters
    num_v : int()
        Number of vertices
    prev : list()
        Vertices and its previous vertex, will be used to reconstruc an edge
    dist : list()
        Vertices and their distance to the starting point
    sets : list()
        Set of each vertex

    Methods
    -------
    union(self, vertex, neighbor):
        Merge two subtrees with union by rank heuristic and path comprehension.
    get_cluster(self, vertex):
        Returns the true cluster of the vertex.
    kruskal(self):
        Kruskal algorithm to find the minimum distance separating a cluster group.
    prim(self):
        Prim algorithm to create a minimal spanning tree.

    """

    def __init__(self, vertices, n_cls, n_vr):
        """
        Constructs all the necessary attributes for a minimum spanning tree:

        Parameters
        ----------
        vertices : list()
            Vertices and their coordinates on the x and y axes
        num_clus : int()
            Number if clusters
        num_v : int()
            Number of vertices
        prev : list()
            Vertices and its previous vertex, will be used to reconstruc an edge
        dist : list()
            Vertices and their distance to the starting point
        sets : list()
            Set of each vertex
        """

        self.vertices = vertices
        self.num_clus = n_cls
        self.num_v = n_vr
        self.prev = [None for _ in range(self.num_v)]
        self.dist = [float('inf') for _ in range(self.num_v)]
        self.sets = [i for i in range(self.num_v)]


    def union(self, vertex, neighbor):
        '''Merge two subtrees with union by rank heuristic and path comprehension.'''

        ranks = [1 for i in range(self.num_v)]

        # merge the smallest subtrees to the largest
        if ranks[vertex] >= ranks[neighbor]:
            ranks[vertex] += ranks[neighbor] # increase the rank of the root vertex
            ranks[neighbor] = 0 # rank of the child vertex at 0
            self.sets[neighbor] = vertex  # compress path

        else:
            ranks[neighbor] += ranks[vertex]
            ranks[vertex] = 0
            self.sets[vertex] = neighbor


    def get_cluster(self, vertex):
        '''Returns the true cluster of the vertex.'''

        cluster = self.sets[vertex]
        # keep going until find the true cluster
        while vertex != cluster:
            vertex = cluster
            cluster = self.sets[vertex]

        return cluster # true cluster


    def kruskal(self):
        '''Kruskal algorithm to find the minimum distance separating a cluster group'''

        count_clus = self.num_v
        edges = list()
        heapq.heapify(edges)
        for ver in range(1, self.num_v): # 1 since we are not interested in the root
            weight = [self.dist[ver], ver] # pair [distance, vertex]
            heapq.heappush(edges, weight)

        if count_clus == self.num_clus: # we already have the desired number of clusters
            min_weight = heapq.heappop(edges) # the pair with the shortest distance
            distance = min_weight[0] # minimum distance between clusters
            return distance

        while edges:
            min_weight = heapq.heappop(edges)
            vertex = min_weight[1]
            neighbor = self.prev[vertex]
            # edge = (vertex, neighbor)

            ver_parent = self.get_cluster(vertex)
            nei_parent = self.get_cluster(neighbor)

            # only join them if they are part of different clusters
            if ver_parent != nei_parent:
                self.union(ver_parent, nei_parent)
                 # with each union call the number of clusters decreases.
                count_clus -= 1
                if count_clus == self.num_clus: # we reach the desired number of clusters
                    min_weight = heapq.heappop(edges)
                    distance = min_weight[0] # minimum distance between clusters
                    return distance


    def prim(self):
        '''Prim algorithm to create a minimal spanning tree'''

        visited = dict()
        root = 0 # starting point
        self.dist[root] = 0
        min_heap = list()
        heapq.heapify(min_heap)
        cost = [self.dist[root], root] # pair [distance, vertex]
        heapq.heappush(min_heap, cost)

        while min_heap:
            min_vertex = heapq.heappop(min_heap) # the pair with the shortest distance
            vertex = min_vertex[1]
            visited[vertex] = 'visited'
            v_x = self.vertices[vertex][0] # x-axis coordinates
            v_y = self.vertices[vertex][1] # y-axis coordinates

            for neighbor in range(self.num_v):
                n_x = self.vertices[neighbor][0]
                n_y = self.vertices[neighbor][1]

                # the length of a segment with endpoints (𝑥1, 𝑦1) and (𝑥2, 𝑦2)
                # is equal to √︀(𝑥1 − 𝑥2)^2 + (𝑦1 − 𝑦2)^2.
                length = ((v_x - n_x)**2 + (v_y - n_y)**2)**0.5

                if neighbor not in visited and self.dist[neighbor] > length:
                    self.dist[neighbor] = length
                    self.prev[neighbor] = vertex
                    cost = [self.dist[neighbor], neighbor]
                    heapq.heappush(min_heap, cost)

        result = self.kruskal()
        return result


if __name__ == '__main__':
    graph = sys.stdin.read()
    data = list(map(int, graph.split()))
    n_ver = data[0]
    data = data[1:]
    x = data[0:2 * n_ver:2]
    y = data[1:2 * n_ver:2]
    points = list()
    for i in range(n_ver):
        point = [x[i], y[i]]
        points.append(point)
    data = data[2 * n_ver:]
    n_clus = data[0]
    path = Paths(points, n_clus, n_ver)
    print("{0:.9f}".format(path.prim()))
