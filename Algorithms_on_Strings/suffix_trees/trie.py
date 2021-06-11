#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    '''Construct a trie from a collection of patterns. Returns the adjacency
    list corresponding to trie(patterns)'''

    trie = dict()
    root = 0
    trie[root] = dict()

    new_node = 1
    for pattern in patterns:
        node = root

        for index in range(len(pattern)):
            symbol = pattern[index]

            if symbol in trie[node]:
                node = trie.get(node).get(symbol)

            else:
                trie[new_node] = dict() # new node
                trie[node][symbol] = new_node # edge to the new node
                node = new_node
                new_node += 1

    return trie


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
