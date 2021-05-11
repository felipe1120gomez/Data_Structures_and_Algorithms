#!/usr/bin/python3

class Node:
    """
    A class to represent a binary search tree.

    ...

    Attributes
    ----------
    key : list()
        Node list (tree)
    left : list()
        Index list of left children in key
    right : list()
        Index list of right children in key

    Methods
    -------

    """
    def __init__(self, ky, lf, rg):
        """
        Constructs all the necessary attributes for the binary search tree:

        Parameters
        ----------
        key : list()
            Node list (tree)
        left : list()
            Index list of left children in key
        right : list()
            Index list of right children in key

        """

        self.key = ky
        self.left = lf
        self.right = rg


def is_binary_search_tree(tree):
    '''Checks if a binary tree is a binary search tree in the special case with duplicate nodes
    for any node of the tree, if its key is 𝑥, then for any node in its left subtree its key
    must be strictly less than 𝑥, and for any node in its right subtree its key must be greater
    than or equal to 𝑥. In other words, smaller elements are to the left, bigger elements
    are to the right, and duplicates are always to the right'''

    # we start at the root
    stack = [(float('-inf'), tree[0], float('inf'))]

    while stack:
        # we walk the tree from right to left
        cur_min, root, cur_max = stack.pop()
        if root.key < cur_min or root.key >= cur_max:
            return False
        if root.left != -1:
            # we update the maximum
            stack.append((cur_min, tree[root.left], root.key))
        if root.right != -1:
            # we update the minimum
            stack.append((root.key, tree[root.right], cur_max))

    return True


if __name__ == '__main__':
    n_nodes = int(input())
    nodes = [0 for _ in range(n_nodes)]
    for i in range(n_nodes):
        node, l_index, r_index = map(int, input().split())
        # like a named tuple: key = node, left = l_index, right = r_index
        node = Node(node, l_index, r_index)
        nodes[i] = node
    if n_nodes == 0 or is_binary_search_tree(nodes):
        print('CORRECT')
    else:
        print('INCORRECT')
