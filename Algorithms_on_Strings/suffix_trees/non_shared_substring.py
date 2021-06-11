# python3

import sys
import threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class SuffixTree():
    """
    A class to represent a suffix tree.

    ...

    Classes
    -------
    Node():
        A class to represent a node in the tree.

    Attributes
    ----------
    leaves : list()
        Leaves on the tree, nodes without leading edge
    root : SuffixTree instance
        Root of the tree with label None and an edge to the longest suffix in the tree (root.edge)
    root.edge : dict()
        Trie for just longest suffix (text), edge from root to node (text) is text[0]
        Key in dict() is text[0], value is node with label text

    Methods
    -------
    build_suffix_tree(self, text):
        Make suffix tree, without suffix links, from text in quadratic time and linear space.
    explore(self, node):
        Depth-first search in a directed acyclic graph.
    non_shared_sub_string(self):
        Finds the shortest substring of text_one that does not appear in text_two.

    """

    class Node():
        """
        A class to represent a node in the tree.

        ...

        Attributes
        ----------
        label : SuffixTree instance
            Label on path leading to this node
        edge : dict()
            Outgoing edges; maps characters to nodes, Key = characters, value = node
        side : str()
            When we create the tree, all the nodes are part of the text_one
        visited : boolean
            Indicates whether a node has been visited by the explore() function
        parent : node
             parent of the node

        Methods
        -------

        """

        def __init__(self, lab):
            self.label = lab
            self.edge = dict()
            self.side = 'text_one'
            self.visited = False
            self.parent = None


    def __init__(self, text):
        self.leaves = list()
        self.root = self.Node(None)
        self.root.edge[text[0]] = self.Node(text)


    def build_suffix_tree(self, text):
        '''Make suffix tree, without suffix links, from text in quadratic time
            and linear space'''

        # add the rest of the suffixes, from longest to shortest
        for s_start in range(1, len(text)):

            # start at root; we’ll walk down as far as we can go
            node = self.root
            next_s_start = s_start

            while next_s_start < len(text):

                if text[next_s_start] in node.edge:
                    child = node.edge[text[next_s_start]]
                    label = child.label
                    # Walk along edge until we exhaust edge label or
                    # until we mismatch
                    next_next_start = next_s_start + 1

                    while next_next_start - next_s_start < len(label) and text[next_next_start] == label[next_next_start - next_s_start]:
                        next_next_start += 1

                    if next_next_start - next_s_start == len(label):
                        node = child # we exhausted the edge
                        next_s_start = next_next_start
                    else:
                        # we fell off in middle of edge
                        prev_edge = label[next_next_start - next_s_start]
                        new_edge = text[next_next_start]
                        # create “mid”: new node bisecting edge
                        mid = self.Node(label[:next_next_start - next_s_start])
                        mid.edge[new_edge] = self.Node(text[next_next_start:])
                        # original child’s label is curtailed
                        child.label = label[next_next_start - next_s_start:]
                        # prev_edge becomes mid’s edge
                        mid.edge[prev_edge] = child
                        # mid becomes new edge of original node
                        node.edge[text[next_s_start]] = mid
                else:
                    # Fell off tree at a node: make new edge hanging off it
                    node.edge[text[next_s_start]] = self.Node(text[next_s_start:])


    def explore(self, node):
        '''Depth-first search in a directed acyclic graph'''

        node.visited = True

        if len(node.edge) == 0:
            if '#' not in node.label:
                node.side = 'text_two'
            else:
                self.leaves.append(node)

        else:
            for label, edge in node.edge.items():
                if not edge.visited:
                    edge.parent = node
                    self.explore(edge)

            for label, edge in node.edge.items():
				# If a child node belongs to text_two his parent also
                if edge.side == 'text_two':
                    node.side = 'text_two'


    def non_shared_sub_string(self):
        '''Finds the shortest substring of text_one that does not appear in text_two'''

        # first the tree is explored to know to which text each node belongs and its parent
        self.explore(self.root)

        strings = []

        for leaf in self.leaves:
            char = str()
            substring = str()
            node = leaf.parent

            # a node between text_one and text_two
            if leaf.label[0] == '#' and node.side == 'text_two':
                continue
            elif node.side == 'text_two':
                char += leaf.label[0]

            while node != self.root: # go up to the root
                substring = node.label + substring
                node = node.parent
            substring += char
            strings.append(substring)

        shortest = min(strings, key=lambda x:len(x))

        return shortest


if __name__ =='__main__':
    text_one = input().strip()
    text_two = input().strip()
    new_text = text_one + '#' + text_two + '$'
    stree = SuffixTree(new_text)
    stree.build_suffix_tree(new_text)
    print(stree.non_shared_sub_string())
