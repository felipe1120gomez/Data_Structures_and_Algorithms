# python3


def build_trie(pat_list):
    '''Construct a trie from a collection of patterns. Returns the trie'''

    trie = dict()
    root = 0
    trie[root] = dict()

    new_node = 1
    for pattern in pat_list:
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


def prefix_matching(cur_text, trie):
    '''Loops through the given portion of text and returns
    whether there is a pattern in it or not.'''

    index = 0
    node = 0 # root of the tree
    symbol = cur_text[index]

    while True:

        if not trie[node]: # if it is a leaf, there is nothing after
            return True

        next_node = trie.get(node).get(symbol)
        if next_node in trie:
            index += 1
            symbol = cur_text[index]
            node = next_node

        else:
            return False # mismatch


def solve(gen_text, pat_list):
    '''Loops through the text and returns a list of
    indices where the patterns start in the text.'''

    trie = build_trie(pat_list)

    matches = []

    # mark indicating the end of the text
    gen_text = gen_text + '$'

    index = 0

    while gen_text:

        if prefix_matching(gen_text, trie):
            matches.append(index)
        index += 1
        gen_text = gen_text[1:] # removes the first letter from the text

    return matches


if __name__ == '__main__':
    text = input().strip()
    n = int (input().strip())
    patterns = [input().strip() for _ in range(n)]
    prefixes = solve(text, patterns)
    print(' '.join(map(str, prefixes)) + '\n')
