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
    prev : dict()
        Vertex and value assigned at the beginning of the exploration
    post : dict()
        Vertex and value assigned at the end of the exploration
    visited : dict()
        Visited vertices
    clock : 1
        Value that is assigned to each vertex in previsit and postvisit,
        increases by one after each assignment
    cyclic : False
        It is assumed that the graph to be traversed is not cyclical,
        this value will change if a cycle is found

    Methods
    -------
    previsit(self, vertex):
        Assigns each vertex the current value of the clock when the exploration starts.
    postvisit(self, vertex):
        Assigns each vertex the current value of the clock when the exploration ends.
    explore(self, vertex):
        Traverse each neighbor of a given vertex and check if there is a cycle.
    acyclic(self, num):
        Returns 1 if there is a cycle otherwise 0.

    """

    def __init__(self, adj_l):
        """
        Constructs all the necessary attributes for a directed graph:

        Parameters
        ----------
        adj_list : list()
            Vertices and their neighbors
        prev : dict()
            Vertex and value assigned at the beginning of the exploration
        post : dict()
            Vertex and value assigned at the end of the exploration
        visited : dict()
            Visited vertices
        clock : 1
            Value that is assigned to each vertex in previsit and postvisit,
            increases by one after each assignment
        cyclic : False
            It is assumed that the graph to be traversed is not cyclical,
            this value will change if a cycle is found
        """

        self.adj_list = adj_l
        self.prev = dict()
        self.post = dict()
        self.visited = dict()
        self.clock = 1
        self.cyclic = False

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
        '''Traverse each neighbor of a given vertex and check if there is a cycle.'''

        self.visited[vertex] = 'visited'
        self.previsit(vertex)

        for neighbor in self.adj_list[vertex]:
            # If there is a cycle, we return on every recursive call
            # to avoid unnecessary iterations.
            if self.cyclic:
                return
            # If we rediscover a vertex that has not been fully explored,
            # that means there is a cycle.
            if neighbor in self.prev and neighbor not in self.post:
                self.cyclic = True
                return
            elif neighbor not in self.visited:
                self.explore(neighbor)

        self.postvisit(vertex)

    def acyclic(self, num):
        '''Returns 1 if there is a cycle otherwise 0.'''

        for vertex in range(0, num): # vertex = index in the list
            if vertex not in self.visited:
                self.explore(vertex)
                if self.cyclic:
                    return 1

        return 0

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
    print(d_graph.acyclic(n_ver))
