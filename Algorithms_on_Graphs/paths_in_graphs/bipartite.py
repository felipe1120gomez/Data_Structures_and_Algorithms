#Uses python3

import sys
from collections import deque

class Bfs:
    """
    A class to represent a breadth first search.

    ...

    Attributes
    ----------
    adj_list : list()
        Vertices and their neighbors
    num_v : int()
        Number of vertices
    visited : dict()
        Visited vertices
    color : list()
        Vertices and their colors
    process : deque()
        Queue to explore vertices in the order they are discovered

    Methods
    -------
    bf_search(self, ver):
        Breadth first search, explores all neighboring vertices to the give vertex,
        gives a color to each vertex and determines if the graph is bipartite.
    bipartite(self):
        Traverse the entire graph with a depth first search, and call
        the bf_search function with each vertex not traversed.

    """

    def __init__(self, adj_l, n_vr):
        """
        Constructs all the necessary attributes for a breadth first search:

        Parameters
        ----------
        adj_list : list()
            Vertices and their neighbors
        num_v : int()
            Number of vertices
        visited : dict()
            Visited vertices
        color : list()
            Vertices and their colors
        process : deque()
            Queue to explore vertices in the order they are discovered
        """

        self.adj_list = adj_l
        self.num_v = n_vr
        self.visited = dict()
        self.color = [None for _ in range(self.num_v)]
        self.process = deque()

    def bf_search(self, ver):
        '''Breadth first search, explores all neighboring vertices to the give vertex,
        gives a color to each vertex and determines if the graph is bipartite.'''

        self.color[ver] = 1
        self.process.append(ver)

        while self.process:
            vertex = self.process.popleft()
            self.visited[vertex] = 'visited'

            for neighbor in self.adj_list[vertex]:
                if self.color[neighbor] is None:
                    self.process.append(neighbor)
                    # opposite color to its origin vertex
                    self.color[neighbor] = self.color[vertex] * -1
                else:
                    # if it has the same color the graph is not bipartite
                    if self.color[neighbor] == self.color[vertex]:
                        return False

        return True

    def bipartite(self):
        '''Traverse the entire graph with a depth first search, and call
        the bf_search function with each vertex not traversed.'''

        # this function is needed to traverse isolated vertices
        for vertex in range(0, self.num_v): # vertex = index in the list
            if vertex not in self.visited:
                if not self.bf_search(vertex):
                    return 0

        return 1

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
    bi_graph = Bfs(adj, n_ver)
    print(bi_graph.bipartite())
