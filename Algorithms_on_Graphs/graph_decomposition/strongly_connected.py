#Uses python3

import sys

sys.setrecursionlimit(200000)

class Dgraph:
    """
    A class to represent a directed graph.

    ...

    Attributes
    ----------
    num_v : int()
        Number of vertices
    adj_list : list()
        Vertices and their neighbors
    t_sort : list()
        Vertices sorted in descending order according to their post value
    g_rev : list()
        Graph with its edges reversed
    prev : dict()
        Vertex and value assigned at the beginning of the exploration
    post : dict()
        Vertex and value assigned at the end of the exploration
    visited : dict()
        Visited vertices
    component : dict()
        Vertex and the component to which it belongs
    clock : 1
        Value that is assigned to each vertex in previsit and postvisit,
        increases by one after each assignment

    Methods
    -------
    previsit(self, vertex):
        Assigns each vertex the current value of the clock when the exploration starts.
    postvisit(self, vertex):
        Assigns each vertex the current value of the clock when the exploration ends.
    explore_rev(self, vertex):
        Traverse each neighbor of the given vertex, reverse the edges of the graph,
        and order the vertices according to their post value.
    dfs_rev(self):
        Traverse each vertex of the graph.
    explore(self, vertex, id_c):
        Traverse each neighbor of a given vertex.
    strongly_connected_components(self):
        Returns the number of strongly connected components of a graph.

    """

    def __init__(self, adj_l, num):
        """
        Constructs all the necessary attributes for a directed graph:

        Parameters
        ----------
        num_v : int()
            Number of vertices
        adj_list : list()
            Vertices and their neighbors
        t_sort : list()
            Vertices sorted in descending order according to their post value
        g_rev : list()
            Graph with its edges reversed
        prev : dict()
            Vertex and value assigned at the beginning of the exploration
        post : dict()
            Vertex and value assigned at the end of the exploration
        visited : dict()
            Visited vertices
        component : dict()
            Vertex and the component to which it belongs
        clock : 1
            Value that is assigned to each vertex in previsit and postvisit,
            increases by one after each assignment
        """

        self.num_v = num
        self.adj_list = adj_l
        self.t_sort = list()
        self.g_rev = [[] for _ in range(self.num_v)]
        self.prev = dict()
        self.post = dict()
        self.visited = dict()
        self.component = dict()
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

    def explore_rev(self, vertex):
        '''Traverse each neighbor of the given vertex, reverse the edges of the graph,
        and order the vertices according to their post value.'''

        self.visited[vertex] = 'visited'
        self.previsit(vertex)

        for neighbor in self.adj_list[vertex]:
            self.g_rev[neighbor].append(vertex)
            if neighbor not in self.visited:
                self.explore_rev(neighbor)

        self.postvisit(vertex)

        if len(self.t_sort) == 0:
            self.t_sort.append(vertex)
        else:
            for i in range(len(self.t_sort)):
                pre_vertex = self.t_sort[i]
                if self.post[pre_vertex] < self.post[vertex]:
                    self.t_sort.insert(i, vertex)
                    break

    def dfs_rev(self):
        '''Traverse each vertex of the graph.'''

        for vertex in range(0, self.num_v): # vertex = index in the list
            if vertex not in self.visited:
                self.explore_rev(vertex)

        self.visited.clear()

    def explore(self, vertex, id_c):
        '''Given a vertex and the id of a component, explore the neighbors
        of the vertex and establish which component they belong to.'''

        self.visited[vertex] = 'visited'
        self.component[vertex] = id_c

        for neighbor in self.g_rev[vertex]:
            if neighbor not in self.visited:
                self.explore(neighbor, id_c)

    def strongly_connected_components(self):
        '''Increases the number of connected components with each call of the
        Explore function, returns the number of strongly connected components of a graph.'''

        self.dfs_rev() # First you have to reverse the graph

        id_comp = 1

        # We go through the reverted graph in the order indicated by t_sort
        for vertex in self.t_sort: # vertex = index in the list
            if vertex not in self.visited:
                self.explore(vertex, id_comp)
                # if we cannot go through the entire graph in one call, it has more than one component
                id_comp += 1

        return id_comp - 1 # we subtract the last iteration


if __name__ == '__main__':
    graph = sys.stdin.read()
    data = list(map(int, graph.split()))
    n_ver, n_edg = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * n_edg):2], data[1:(2 * n_edg):2]))
    adj = [[] for _ in range(n_ver)] # list of vertices and their neighbors
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    d_graph = Dgraph(adj, n_ver)
    print(d_graph.strongly_connected_components())
