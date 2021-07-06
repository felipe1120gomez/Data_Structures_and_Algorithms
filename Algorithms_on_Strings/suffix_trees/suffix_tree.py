# python3


from collections import deque

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
    root : SuffixTree instance
        Root of the tree with label None and an edge to the longest suffix in the tree (root.edge)
    root.edge : dict()
        Trie for just longest suffix (text), edge from root to node (text) is text[0]
        Key in dict() is text[0], value is node with label text

    Methods
    -------
    build_suffix_tree(self, text):
        Make suffix tree, without suffix links, from text in quadratic time and linear space.
    print_labels(self):
        Walk the tree and print the label on each edge.

    """

    class Node():
        """
        A class to represent a node in the tree.

        ...

        Attributes
        ----------
        label : Node instance
            Label on path leading to this node
        edge : dict()
            Outgoing edges; maps characters to nodes, Key = characters, value = node

        Methods
        -------

        """

        def __init__(self, lab):
            self.label = lab
            self.edge = dict()


    def __init__(self, text):
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


    def print_labels(self):
        '''Walk the tree and print the label on each edge'''

        tree = deque()
        tree.append(self.root)

        while tree:
            node = tree.popleft()

            if node != self.root:
                print(node.label)

            for label, edge in node.edge.items():
                tree.append(edge)


if __name__ =='__main__':
    gen_text = input().strip()
    stree = SuffixTree(gen_text)
    stree.build_suffix_tree(gen_text)
    stree.print_labels()
