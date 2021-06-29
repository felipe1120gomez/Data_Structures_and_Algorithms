#uses python3

import sys
import threading


sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    weight : int()
        Node weight
    sub_tree : list()
        List of his children and also his father

    Methods
    -------
    """

    def __init__(self, weight):
        self.weight = weight
        self.children = []

class FunParty:
    """
    A class to represent a tree with weighted nodes.

    ...

    Attributes
    ----------
    p_tree : list()
        List of nodes and their children
    sub_tree : list()
        List to keep track of the highest weights obtained

    Methods
    -------
    dfs(self, vertex, parent):
        Depth-first search.
    max_weight_independent_tree_subset(self):
        Gets the maximum value in a tree with the condition that a
        parent node and its children cannot be part of the same subset.
    """

    def __init__(self, party_tree, num_v):
        self.p_tree = party_tree
        self.sub_tree = [None for _ in range(num_v)]


    def dfs(self, vertex, parent):
        '''Depth-first search'''

        if self.sub_tree[vertex] is None:

            list_child = self.p_tree[vertex].children
            # if the node has no children, its maximum weight will be its own
            if len(list_child) == 1 and list_child[0] == parent or not list_child:
                self.sub_tree[vertex] = self.p_tree[vertex].weight
                return self.sub_tree[vertex]

            weight_grandchildrens = self.p_tree[vertex].weight

            # sum of the weights of its grandchildren
            for child in self.p_tree[vertex].children:
                if child in (parent, vertex):
                    continue
                for grand_child in self.p_tree[child].children:
                    if grand_child in (vertex, child):
                        continue
                    weight_grandchildrens += self.dfs(grand_child, child)

            weight_childrens = 0

            # sum of its children's weights
            for child in self.p_tree[vertex].children:
                if child in (parent, vertex):
                    continue
                weight_childrens +=  self.dfs(child, vertex)

            # the highest value is chosen among children and grandchildren
            self.sub_tree[vertex] = max(weight_grandchildrens, weight_childrens)

        return self.sub_tree[vertex]


    def max_weight_independent_tree_subset(self):
        '''Gets the maximum value in a tree with the condition that a
        parent node and its children cannot be part of the same subset.'''

        size = len(self.p_tree)

        if size == 0:
            return 0
        if size == 1:
            return self.p_tree[0].weight

        max_fun = self.dfs(0, -1)

        return max_fun


def main():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for _ in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1) # The father is also added to the list of children
        tree[b - 1].children.append(a - 1)
    party = FunParty(tree, len(tree))
    weight = party.max_weight_independent_tree_subset()
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
