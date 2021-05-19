#Uses python3

import sys

class Maze:
    """
    A class to represent a maze.

    ...

    Attributes
    ----------
    adj_list : list()
        Vertices and their neighbors
    component : dict()
        Vertex and the component to which it belongs
    visited : dict()
        Visited vertices

    Methods
    -------
    explore(self, vertex, id_c):
        Traverse each neighbor of a given vertex.
    reach(self, num, start_vertex, end_vertex):
        Given a starting vertex and an arrival vertex, check that they are connected.

    """

    def __init__(self, adj_l):
        """
        Constructs all the necessary attributes for a maze:

        Parameters
        ----------
        adj_list : list()
            Vertices and their neighbors
        component : dict()
            Vertex and the component to which it belongs
        visited : dict()
            Visited vertices
        """

        self.adj_list = adj_l
        self.component = dict()
        self.visited = dict()

    def explore(self, vertex, id_c):
        '''Given a vertex and the id of a component, explore the neighbors
        of the vertex and establish which component they belong to.'''

        self.visited[vertex] = 'visited'
        self.component[vertex] = id_c

        for neighbor in self.adj_list[vertex]:
            if neighbor not in self.visited:
                self.explore(neighbor, id_c)

    def reach(self, num, start_vertex, end_vertex):
        '''Given a starting vertex and an arrival vertex, check that they are connected'''

        id_comp = 1

        for vertex in range(0, num): # vertex = index in the list
            if vertex not in self.visited:
                self.explore(vertex, id_comp)
                # if we cannot go through the entire graph in one call, it has more than one component
                id_comp += 1

        # if they belong to the same component they are connected
        if self.component[start_vertex] == self.component[end_vertex]:
            return 1

        return 0

if __name__ == '__main__':
    graph = sys.stdin.read()
    data = list(map(int, graph.split()))
    n_ver, n_edg = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * n_edg):2], data[1:(2 * n_edg):2]))
    x, y = data[2 * n_edg:]
    adj = [[] for _ in range(n_ver)] # list of vertices and their neighbors
    start, end = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    maze = Maze(adj)
    print(maze.reach(n_ver, start, end))
