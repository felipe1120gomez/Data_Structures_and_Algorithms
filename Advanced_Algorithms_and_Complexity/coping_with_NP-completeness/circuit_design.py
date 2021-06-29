#Uses python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class Dgraph:
    """
    A class to represent a directed graph.

    ...

    Attributes
    ----------
    num_v : int()
        Number of vertices
    neg_v : int()
        Negative vertex range
    adj_list : dict()
        Vertices and their neighbors
    t_sort : list()
        Vertices sorted in descending order according to their post value (topological sort)
    g_rev : dict()
        Graph with its edges reversed
    prev : dict()
        Vertex and value assigned at the beginning of the exploration
    post : dict()
        Vertex and value assigned at the end of the exploration
    visited : dict()
        Visited vertices
    component : dict()
        Vertex and the component to which it belongs
    component_2 : dict()
        Component and list of vertices that belong to it
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
        and order the vertices according to their post value (topological sort).
    dfs_rev(self):
        Traverse each vertex of the graph.
    explore(self, vertex, id_c):
        Traverse each neighbor of a given vertex.
    strongly_connected_components(self):
        Find the strongly connected components in the graph.
    two_sat(self):
        Determine if a 2-CNF formula is satisfiable by examining some possible values for its variables.
    """

    def __init__(self, adj_l, num):
        """
        Constructs all the necessary attributes for a directed graph:

        Parameters
        ----------
        num_v : int()
            Number of vertices
        neg_v : int()
            Negative vertex range
        adj_list : dict()
            Vertices and their neighbors
        t_sort : list()
            Vertices sorted in descending order according to their post value (topological sort)
        g_rev : dict()
            Graph with its edges reversed
        prev : dict()
            Vertex and value assigned at the beginning of the exploration
        post : dict()
            Vertex and value assigned at the end of the exploration
        visited : dict()
            Visited vertices
        component : dict()
            Vertex and the component to which it belongs
        component_2 : dict()
            Component and list of vertices that belong to it
        clock : 1
            Value that is assigned to each vertex in previsit and postvisit,
            increases by one after each assignment
        """

        self.num_v = num
        self.neg_v = num * -1
        self.adj_list = adj_l
        self.t_sort = list()
        self.g_rev = {i : list() for i in range(self.neg_v, self.num_v + 1) if i != 0}
        self.prev = dict()
        self.post = dict()
        self.visited = dict()
        self.component = dict()
        self.component_2 = dict()
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

        for neighbor in self.adj_list.get(vertex):
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

        vertices = [i for i in range(self.neg_v, self.num_v + 1) if i != 0]

        for vertex in vertices:
            if vertex not in self.visited:
                self.explore_rev(vertex)

        self.visited.clear()

    def explore(self, vertex, id_c):
        '''Given a vertex and the id of a component, explore the neighbors
        of the vertex and establish which component they belong to.'''

        self.visited[vertex] = 'visited'
        self.component[vertex] = id_c

        if id_c not in self.component_2: # component and its list of vertices
            self.component_2[id_c] = list()
            self.component_2[id_c].append(vertex)

        else:
            self.component_2[id_c].append(vertex)

        for neighbor in self.g_rev.get(vertex):
            if neighbor not in self.visited:
                self.explore(neighbor, id_c)

    def strongly_connected_components(self):
        '''Find the strongly connected components in the graph.'''

        self.dfs_rev() # First you have to reverse the graph

        id_comp = 1

        # We go through the reverted graph in the order indicated by t_sort
        for vertex in self.t_sort: # vertex = index in the list
            if vertex not in self.visited:
                self.explore(vertex, id_comp)
                # if we cannot go through the entire graph in one call, it has more than one component
                id_comp += 1

        result = self.two_sat()

        if result is False:
            print("UNSATISFIABLE")

        else:
            print("SATISFIABLE")
            print(*result)


    def two_sat(self):
        '''Determine if a 2-CNF formula is satisfiable by
        examining some possible values for its variables.'''

        assigned_vars = dict()
        # If the variable is positive its value is 1,
        # if it is its negative counterpart its value is 0

        com_visited = dict()

        for var_x in range(1, self.num_v + 1):
            # if the variable and its counterpart are in the same strongly connected component
            if self.component.get(var_x) == self.component.get(var_x * -1):
                return False

        self.t_sort = self.t_sort[::-1] # reversed topological sort

        for cur_comp in self.t_sort:
            com_id = self.component.get(cur_comp)
            if com_id not in com_visited:
                com_list = self.component_2.get(com_id)
                com_visited[com_id] = 'visited'

                for cur_var in com_list:
                    # if the variable and its counterpart do not have an assigned value
                    if cur_var not in assigned_vars and cur_var * -1 not in assigned_vars:
                        assigned_vars[cur_var] = 1 # we only assign value to the variable, not for its counterpart

        result = list(assigned_vars.keys())

        return sorted(result, key=abs) # sorted by its absolute value


def main():
    graph = sys.stdin.read()
    data = list(map(int, graph.split()))
    n_var, n_cla = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * n_cla):2], data[1:(2 * n_cla):2]))
    neg = n_var * -1
    adj = {i : list() for i in range(neg, n_var + 1) if i != 0} # list of vertices and their neighbors
    for (a, b) in edges:
        adj[a * -1].append(b)
        adj[b * -1].append(a)
    d_graph = Dgraph(adj, n_var)
    d_graph.strongly_connected_components()

threading.Thread(target=main).start()
