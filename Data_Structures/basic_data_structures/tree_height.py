# python3

from collections import deque

def compute_height(nodes, parents):
    '''Given a description of a rooted tree, compute and return its height.
    Recall that the height of a (rooted) tree is the maximum depth of a node,
    or the maximum distance from a leaf to the root.
    You are given an arbitrary tree, not necessarily a binary tree.'''

    tree = [[] for _ in parents]

    for child_i in range(nodes):
        parent_i = parents[child_i]
        if parent_i == -1: # -1 is the root
            root = child_i # Root index in the tree
        else:
            tree[parent_i].append(child_i) # Each node with its children

    visited = dict()
    deq = deque() # A deque is used to get the element at index 0, in O(1)
    deq.append([root, 0]) # Root level is 0
    max_high = 0
    node_level = list()

    while deq:
        node_level = deq.popleft()
        node = node_level[0] # Node in the tree
        level = node_level[1] # Level of that node
        visited[node] = 'visited' # Node is marked as visited

        max_high = max(max_high, level) # The highest level visited is chosen
        childs = len(tree[node]) # Number of children of the node

        for child in range(childs):
            if tree[node][child] not in visited: # If it has not been visited
                deq.append([tree[node][child], level + 1]) # That node is added and its level is +1

    return max_high + 1

def main():
    n_nodes = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n_nodes, parents))

if __name__ == "__main__":
    main()
