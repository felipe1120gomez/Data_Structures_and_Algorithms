# python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class SuffixTree:
    """

    A class to represent a suffix tree.

    ...

    Classes
    -------
    Node():
        A class to represent a node in the tree.

    Attributes
    ----------
    text : str()
        Text string that will be used to build the suffix tree
    symb : list()
        Symbols that can compose the text string
    suff_arr : list()
        Indexes where each suffix begins in the text, ordered lexicographically
    long_c_pref : list()
        List that stores the length of the longest common prefix shared by
        consecutive lexicographically ordered suffixes of Text
    root : SuffixTree instance:
        Root of the tree with parent None and depth 0


    Methods
    -------
    new_leaf(self, node, suffix):
        Creates a new node in the tree to represent a suffix.
    break_edge(self, node, mid_start, offset):
        Breaks an edge and got 3 nodes: mid, left(exist already), right(new suffix).
    tree_from_array(self):
        Constructs a suffix tree from the suffix array and LCP array of a string.
    print_edges(self, cur):
        Outputs all the edges in the order of sorted suffixes: first, take the leaf of
        the suffix tree corresponding to the smallest suffix of Text and output all the
        edges on the path from the root to this leaf. Then take the leaf corresponding
        to the second smallest suffix of Text and output all the edges on the path from
        the root to this leaf except for those edges which were printed before.
        Then take the leaf corresponding to the third smallest suffix,
        fourth smallest suffix and so on.

    """

    class Node:
        """

        A class to represent a node in the tree.

        ...

        Attributes
        ----------
        parent : Node instance
            Parent of the node in the tree
        children : Dict()
            First suffix symbol as key, nodes created by break_edge() function as values
        depth : int()
            Suffix length
        start : int()
            Index in the text string where the suffix starts
        end : int()
            Index in the text string where the suffix ends
        visited : boolean
            Indicates whether a node has been visited by the print_edges() function


        Methods
        -------

        """

        def __init__(self, node, depth, edge_start, edge_end):
            self.parent = node
            self.children = dict()
            self.depth = depth
            self.start = edge_start
            self.end = edge_end
            self.visited = False

    def __init__(self, in_text, s_array, lcp):
        self.text = in_text
        self.symb = ['$', 'A', 'C', 'G', 'T']
        self.suff_arr = s_array
        self.long_c_pref = lcp
        self.root = self.Node(None, 0, -1, -1)


    def new_leaf(self, node, suffix):
        '''Creates a new node in the tree to represent a suffix.'''

        len_text = len(self.text) # edg_end

        n_depth = len_text - suffix

        edg_start = suffix + node.depth

        leaf = self.Node(node, n_depth, edg_start, len_text)

        node.children[self.text[leaf.start]] = leaf

        return leaf


    def break_edge(self, node, mid_start, offset):
        '''Breaks an edge and got 3 nodes: mid, left(exist already), right(new suffix).'''

        mid_char = self.text[mid_start]

        left_char = self.text[mid_start + offset]

        m_depth = node.depth + offset

        mid_end = mid_start + offset

        mid = self.Node(node, m_depth, mid_start, mid_end)

        mid.children[left_char] = node.children[mid_char]

        node.children[mid_char].parent = mid

        node.children[mid_char].start += offset

        node.children[mid_char] = mid

        return mid


    def tree_from_array(self):
        '''Constructs a suffix tree from the suffix array and LCP array of a string.'''

        lcp_prev = 0

        cur_node = self.root

        len_text = len(self.text)

        for index in range(len_text):

            suffix = self.suff_arr[index]

            while cur_node.depth > lcp_prev:
                cur_node = cur_node.parent

            if cur_node.depth == lcp_prev:
                cur_node = self.new_leaf(cur_node, suffix)

            else:

                mid_start = self.suff_arr[index - 1] + cur_node.depth  # the start of mid-node

                offset = lcp_prev - cur_node.depth  # the number of characters of mid-node

                mid = self.break_edge(cur_node, mid_start, offset)

                cur_node = self.new_leaf(mid, suffix)

            if index < len_text - 1:
                lcp_prev = self.long_c_pref[index]


    def print_edges(self, cur):
        '''Outputs all the edges in the order of sorted suffixes: first, take the leaf
        of the suffix tree corresponding to the smallest suffix of Text and output all
        the edges on the path from the root to this leaf and so on.'''

        cur.visited = True

        if cur != self.root:
            print(cur.start, cur.end)

        # print the children of each node in the order indicated by the symb list,
        # which is the lexicological order
        for symbol in range(5):
            child = cur.children.get(self.symb[symbol], None)

            if child is not None and not child.visited:
                self.print_edges(child)


def main():
    input_text = input()
    suffix_array = list(map(int, input().split()))
    input_lcp = list(map(int, input().split()))
    print(input_text)
    suffix_tree = SuffixTree(input_text, suffix_array, input_lcp)
    suffix_tree.tree_from_array()
    suffix_tree.print_edges(suffix_tree.root)

threading.Thread(target=main).start()
