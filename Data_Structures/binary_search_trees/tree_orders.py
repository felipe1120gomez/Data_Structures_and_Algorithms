# python3

class TreeOrders:
    """
    A class to represent the three ways to traverse a tree.

    ...

    Attributes
    ----------
    nodes : int()
        Number of nodes
    key : list()
        Node list (tree)
    left : list()
        Index list of left children in key
    right : list()
        Index list of right children in key
    roots : dict()
        Dictionary created with key values as key and indexes as value
    lft : dict()
        Dictionary created with left values as key and indexes as value
    rgt : dict()
        Dictionary created with right values as key and indexes as value

    Methods
    -------
    read(self):
        Create a binary tree from the input lines.

    in_order(self):
        First the left node is added, then the root, and finally the right node.

    pre_order(self):
        The root is added first, then the left node and finally the right node.

    post_order(self):
        First the left node is added, then the right node and finally the root.

    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the three ways to traverse a tree:

        Parameters
        ----------
        nodes : int()
            Number of nodes
        key : list()
            Node list (tree)
        left : list()
            Index list of left children in key
        right : list()
            Index list of right children in key
        roots : dict()
            Dictionary created with key values as key and indexes as value
        lft : dict()
            Dictionary created with left values as key and indexes as value
        rgt : dict()
            Dictionary created with right values as key and indexes as value

        """

        self.nodes = int()
        self.key = list()
        self.left = list()
        self.right = list()
        self.roots = dict()
        self.lft = dict()
        self.rgt = dict()

    def read(self):
        '''Each input line contains three integers key, left and right
        key is the key of the 𝑖-th node, left is the index of the left child of the 𝑖-th node,
        and right is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have left or
        right child (or both), the corresponding left or right (or both) will be equal to −1.'''

        self.nodes = int(input())
        self.key = [0 for i in range(self.nodes)]
        self.left = [0 for i in range(self.nodes)]
        self.right = [0 for i in range(self.nodes)]
        for i in range(self.nodes):
            [node, l_index, r_index] = map(int, input().split())
            self.key[i] = node # nodes (tree)
            self.left[i] = l_index # indexes of the right children in key
            self.right[i] = r_index # indexes of the left children in key
        # dictionaries to get the indexes in O(1)
        self.roots = {self.key[j]: j for j in range(self.nodes)}
        self.lft = {self.left[j]: j for j in range(self.nodes)}
        self.rgt = {self.right[j]: j for j in range(self.nodes)}

    def in_order(self):
        '''First the left node is added, then the root, and finally the right node'''

        # dictionaries to get the values in O(1)
        result = dict() # nodes
        visited_left = dict() # index of each node visited by the left
        visited_right = dict() # index of each node visited by the right

        node = self.key[0] # root
        while len(result) < self.nodes:# we stop when the table is full

            k_index = self.roots[node] # k_index to query the left and right tables
            l_index = self.left[k_index] # l_index to get the node in the key table

            if k_index not in visited_left:
                # the node index is marked as visited whether or not it has a child
                visited_left[k_index] = 'visited'

                # we go down to the last left node without adding them
                while l_index != -1:
                    node = self.key[l_index] # left son
                    k_index = self.roots[node]
                    # the node's index is marked as visited
                    visited_left[k_index] = 'visited'
                    l_index = self.left[k_index]

            # we try to find the right child of the current node
            r_index = self.right[k_index] # r_index to get the node in the key table

            if k_index not in visited_right:
                # the node index is marked as visited whether or not it has a child
                visited_right[k_index] = 'visited'

            if r_index != -1: # has a right child

                # if the node has already been visited from the left and right
                if k_index in visited_right and k_index in visited_left:

                    if node not in result:# if it has not been added
                        result[node] = node
                        # if it has a child this will be a node
                        node = self.key[r_index] # right son

                    else: # It has already been added, we choose a new node (we go up one level)

                        if k_index in self.lft:
                            l_index = self.lft[k_index]
                            node = self.key[l_index] # root of current node if this is a left child

                        elif k_index in self.rgt:
                            r_index = self.rgt[k_index]
                            node = self.key[r_index] # root of current node if this is a right child

            # this has no right son
            # the node has already been visited from the left and right
            elif k_index in visited_right and k_index in visited_left:

                if node not in result:# if it has not been added
                    result[node] = node

                # we choose a new node (we go up one level)
                if k_index in self.lft:
                    l_index = self.lft[k_index]
                    node = self.key[l_index] # root of current node if this is a left child

                elif k_index in self.rgt:
                    r_index = self.rgt[k_index]
                    node = self.key[r_index] # root of current node if this is a right child

        return list(result.values())

    def pre_order(self):
        '''The root is added first, then the left node and finally the right node'''

        # dictionaries to get the values in O(1)
        result = dict() # nodes
        visited_left = dict() # index of each node visited by the left
        visited_right = dict() # index of each node visited by the right

        node = self.key[0] # root
        result[node] = node # add root
        while len(result) < self.nodes: # we stop when the table is full

            k_index = self.roots[node] # k_index to query the left and right tables
            l_index = self.left[k_index] # l_index to get the node in the key table

            # we are going down and adding the left nodes
            while l_index != -1 and k_index not in visited_left:
                node = self.key[l_index] # left son
                result[node] = node # it is added
                # the node's index is marked as visited
                visited_left[k_index] = 'visited'
                k_index = self.roots[node]
                l_index = self.left[k_index]

            # we add a right child of the current node (only one)
            r_index = self.right[k_index] # r_index to get the node in the key table
            if r_index != -1 and k_index not in visited_right:
                node = self.key[r_index] # right son
                result[node] = node # it is added
                # the node's index is marked as visited
                visited_right[k_index] = 'visited'

            # There is no right child or it has already been visited
            # we choose a new node (we go up one level)
            elif k_index in self.lft:
                l_index = self.lft[k_index]
                node = self.key[l_index] # root of current node if this is a left child

            elif k_index in self.rgt:
                r_index = self.rgt[k_index]
                node = self.key[r_index] # root of current node if this is a right child

        return list(result.values())

    def post_order(self):
        '''First the left node is added, then the right node and finally the root'''

        # dictionaries to get the values in O(1)
        result = dict() # nodes
        visited_left = dict() # index of each node visited by the left
        visited_right = dict() # index of each node visited by the right

        node = self.key[0] # root
        while len(result) < self.nodes: # we stop when the table is full

            k_index = self.roots[node] # k_index to query the left and right tables
            l_index = self.left[k_index] # l_index to get the node in the key table

            if k_index not in visited_left:
                # the node index is marked as visited whether or not it has a child
                visited_left[k_index] = 'visited'

                # we go down to the last left node without adding them
                while l_index != -1:
                    node = self.key[l_index] # left son
                    k_index = self.roots[node]
                    # the node's index is marked as visited
                    visited_left[k_index] = 'visited'
                    l_index = self.left[k_index]

            # we try to find the right child of the current node
            r_index = self.right[k_index] # r_index to get the node in the key table

            if k_index not in visited_right:
                # the node index is marked as visited whether or not it has a child
                visited_right[k_index] = 'visited'

                if r_index != -1: # if it has a child this will be a node
                    node = self.key[r_index] # right son

                else: # No son
                    continue # we continue with the same node

            # the node has already been visited from the left and right
            elif k_index in visited_right and k_index in visited_left:

                if node not in result:# if it has not been added
                    result[node] = node

                # we choose a new node (we go up one level)
                if k_index in self.lft:
                    l_index = self.lft[k_index]
                    node = self.key[l_index] # root of current node if this is a left child

                elif k_index in self.rgt:
                    r_index = self.rgt[k_index]
                    node = self.key[r_index] # root of current node if this is a right child

        return list(result.values())

if __name__ == '__main__':
    tree = TreeOrders()
    tree.read()
    print(*tree.in_order())
    print(*tree.pre_order())
    print(*tree.post_order())
