#Uses python3

import sys

class Dgraph:
    """
    A class to represent a directed graph.

    ...

    Attributes
    ----------
    adj_list : list()
        Vertices and their neighbors
    t_sort : list()
        Vertices sorted in descending order according to their post value
    prev : dict()
        Vertex and value assigned at the beginning of the exploration
    post : dict()
        Vertex and value assigned at the end of the exploration
    visited : dict()
        Visited vertices
    clock : 1
        Value that is assigned to each vertex in previsit and postvisit,
        increases by one after each assignment

    Methods
    -------
    previsit(self, vertex):
        Assigns each vertex the current value of the clock when the exploration starts.
    postvisit(self, vertex):
        Assigns each vertex the current value of the clock when the exploration ends.
    explore(self, vertex):
        Traverse each neighbor of the given vertex and order
        the vertices according to their post value (topsort).
    dfs(self, num):
        Traverse each vertex of the graph and returns a topsort list.

    """

    def __init__(self, adj_l):
        """
        Constructs all the necessary attributes for a directed graph:

        Parameters
        ----------
        adj_list : list()
            Vertices and their neighbors
        t_sort : list()
            Vertices sorted in descending order according to their post value
        prev : dict()
            Vertex and value assigned at the beginning of the exploration
        post : dict()
            Vertex and value assigned at the end of the exploration
        visited : dict()
            Visited vertices
        clock : 1
            Value that is assigned to each vertex in previsit and postvisit,
            increases by one after each assignment
        """

        self.adj_list = adj_l
        self.t_sort = list()
        self.prev = dict()
        self.post = dict()
        self.visited = dict()
        self.clock = 1

    def previsit(self, vertex):
        '''Assigns each vertex the current value of the clock when the exploration starts
        and increases the clock value by one.'''

        self.prev[vertex] = self.clock
        self.clock += 1

    def postvisit(self, vertex):
        '''Assigns each vertex the current value of the clock when the exploration ends
        and increases the clock value by one.'''

        self.post[vertex] = self.clock
        self.clock += 1

    def explore(self, vertex):
        '''Traverse each neighbor of the given vertex and order
        the vertices according to their post value (topsort).'''

        self.visited[vertex] = 'visited'
        self.previsit(vertex)

        for neighbor in self.adj_list[vertex]:
            if neighbor not in self.visited:
                self.explore(neighbor)

        self.postvisit(vertex)

        if len(self.t_sort) == 0:
            self.t_sort.append(vertex + 1) # we add one to save the vertex not its index.
        else:
            for i in range(len(self.t_sort)):
                pre_vertex = self.t_sort[i]
                if self.post[pre_vertex - 1] < self.post[vertex]:
                    self.t_sort.insert(i, vertex + 1) # we add one to save the vertex not its index.
                    break

    def dfs(self, num):
        '''Traverse each vertex of the graph and returns a topsort list.'''

        for vertex in range(0, num): # vertex = index in the list
            if vertex not in self.visited:
                self.explore(vertex)

        return self.t_sort

if __name__ == '__main__':
    graph = sys.stdin.read()
    data = list(map(int, graph.split()))
    n_ver, n_edg = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * n_edg):2], data[1:(2 * n_edg):2]))
    adj = [[] for _ in range(n_ver)] # list of vertices and their neighbors
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    d_graph = Dgraph(adj)
    print(* d_graph.dfs(n_ver))
