# python3

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    """
    A class to represent a vertex of a tree.

    ...

    Attributes
    ----------
    key : int()
        Node
    sum_tree : int()
        Sum of the nodes of the subtree
    left : int()
        Left child pointer
    right : int()
        Right child pointer
    parent : int()
        Node parent pointer

    Methods
    -------

    """
    def __init__(self, key, sum_tree, left, right, parent):
        """
        Constructs all the necessary attributes for the vertex:

        Parameters
        ----------
        key : int()
            Node
        sum_tree : int()
            Sum of the nodes of the subtree
        left : int()
            Left child pointer
        right : int()
            Right child pointer
        parent : int()
            Node parent pointer

        """

        (self.key, self.sum_tree, self.left, self.right, self.parent) = (key, sum_tree, left, right, parent)

def update(node):
    '''Updates the vertex values that are modified
    in the functions: small_rotation, split and merge'''

    if node is None:
        return
    node.sum_tree = node.key + (node.left.sum_tree if node.left is not None else 0) + (node.right.sum_tree if node.right is not None else 0)
    if node.left is not None:
        node.left.parent = node
    if node.right is not None:
        node.right.parent = node

def small_rotation(node):
    '''Perform left or right rotations.'''

    parent = node.parent
    if parent is None:
        return
    grandparent = node.parent.parent
    # rotate to the right
    if parent.left == node:
        childs = node.right
        node.right = parent
        parent.left = childs
    # rotate to the left
    else:
        childs = node.left
        node.left = parent
        parent.right = childs
    update(parent)
    update(node)
    node.parent = grandparent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = node
        else:
            grandparent.right = node

def big_rotation(node):
    '''Perform the following rotations:
    Zig rotation (Right rotation)
    Zag rotation (Left rotation)
    Zig zag (Zig followed by zag)
    Zig zig (two right rotations)
    '''

    if node.parent.left == node and node.parent.parent.left == node.parent:
        # Zig-zig (two right rotations)
        small_rotation(node.parent)
        small_rotation(node)
    elif node.parent.right == node and node.parent.parent.right == node.parent:
        # Zig-zig (two right rotations)
        small_rotation(node.parent)
        small_rotation(node)
    else:
        # Zig-zag (Zig followed by zag)
        small_rotation(node)
        small_rotation(node)

# Makes splay of the given vertex and makes
# it the new root.
def splay(node):
    '''Move the node up until it is root.'''

    if node is None:
        return None
    while node.parent is not None:
        if node.parent.parent is None:
            small_rotation(node)
            break
        big_rotation(node)
    return node

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
    '''Look for a node (key) in the tree and call splay for this node if
    it was found or the previous one if it was not found'''

    node = root
    last = root
    next_n = None
    while node is not None:
        if node.key >= key and (next_n is None or node.key < next_n.key):
            next_n = node
        last = node
        if node.key == key:
            break
        if node.key < key:
            node = node.right
        else:
            node = node.left
    root = splay(last)
    return (next_n, root)

def split(root, key):
    '''Separate the tree in two taking a node (key) as the cutting point'''

    (result, root) = find(root, key)
    if result is None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left is not None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)


def merge(left, right):
    '''Join two trees converting the smallest node from right to root (splay)
    and making left the left child of this new root.'''

    if left is None:
        return right
    if right is None:
        return left
    while right.left is not None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right

# Code that uses splay tree to solve the problem

ROOT = None # Do not use global variables, it is bad practice.

def insert(node):
    '''Use the split operation to split the tree at the value of node
    to two sub-trees: left and right. Create a new tree in which node is the root,
    left is its left sub-tree and right its right sub-tree.'''

    global ROOT

    (left, right) = split(ROOT, node)
    new_vertex = None

    if right is None or right.key != node:
        new_vertex = Vertex(node, node, None, None, None)
    ROOT = merge(merge(left, new_vertex), right)

def erase(node):
    '''Splits the tree into two sub-trees with a common root
    (node to be deleted) merge the trees without the root'''

    global ROOT

    (left, middle) = split(ROOT, node)
    (middle, right) = split(middle, node + 1)

    ROOT = merge(left, right)

def search(node):
    '''Search for a node in the tree by calling the find function'''

    global ROOT

    (result, ROOT) = find(ROOT, node)

    # If the tree is empty or the closest node is not the one we are looking for
    if result is None or result.key != node:
        return False

    return True

def sum_range(start, end):
    '''Split the tree into two subtrees with a common root
    (parent node of the subtree (range) we are looking for)
    if such a root exists the sum of the nodes of that subtree will be the answer,
    merge the trees and the common root'''

    global ROOT

    (left, middle) = split(ROOT, start)
    (middle, right) = split(middle, end + 1)

    ans = 0

    if middle is not None:
        ans += middle.sum_tree

    ROOT = merge(merge(left, middle), right)

    return ans

MODULO = 1000000001
n = int(input())
LAST_SUM_RESULT = 0
for i in range(n):
    line = input().split()
    if line[0] == '+':
        x = int(line[1])
        insert((x + LAST_SUM_RESULT) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + LAST_SUM_RESULT) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + LAST_SUM_RESULT) % MODULO) else 'Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum_range((l + LAST_SUM_RESULT) % MODULO, (r + LAST_SUM_RESULT) % MODULO)
        print(res)
        LAST_SUM_RESULT = res % MODULO
