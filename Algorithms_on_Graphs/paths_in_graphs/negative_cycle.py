#Uses python3

import sys

class Exchange:
    """
    A class to represent a currency exchanger.

    ...

    Attributes
    ----------
    adj_list : list()
        Vertices and their neighbors
    weight : list()
        Weight of each edge
    num_v : int()
        Number of vertices
    dist : list()
        Vertices and their distance to the starting point

    Methods
    -------
    bellman_ford(self):
        Modified Bellman Ford algorithm to check if there is a cycle of negative weight in the graph.

    """

    def __init__(self, adj_l, e_cost, n_vr):
        """
        Constructs all the necessary attributes for a currency exchanger:

        Parameters
        ----------
        adj_list : list()
            Vertices and their neighbors
        weight : list()
            Weight of each edge
        num_v : int()
            Number of vertices
        dist : list()
            Vertices and their distance to the starting point
        """

        self.adj_list = adj_l
        self.weight = e_cost
        self.num_v = n_vr
        self.dist = [0 for _ in range(self.num_v)]
        # is initialized to 0 since there is no specific starting point


    def bellman_ford(self):
        '''Modified Bellman Ford algorithm to find cycles of negative weight in a graph.'''

        for i in range(1, self.num_v + 1): # num_v iterations

            for vertex in range(self.num_v):

                for neighbor in self.adj_list[vertex]:
                    w_neighbor = self.adj_list[vertex].index(neighbor) # neighbor index to check the weight
                    if self.dist[neighbor] > (self.dist[vertex] + self.weight[vertex][w_neighbor]):
                        self.dist[neighbor] = (self.dist[vertex] + self.weight[vertex][w_neighbor])
                        # if iteration num_v modifies any distance, there is a negative cycle
                        if i == (self.num_v):
                            return 1

        return 0


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
    exch = Exchange(adj, cost, n_ver)
    print(exch.bellman_ford())
