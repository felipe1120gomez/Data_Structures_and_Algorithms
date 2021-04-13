# Uses python3

def edit_distance(seq_a, seq_b):
    '''Compute the edit distance between two strings.
    The edit distance between two strings is the minimum number of operations
    (insertions, deletions, and substitutions of symbols) to transform
    one string into another. It is a measure of similarity of two strings.'''

    # 2D table of wide (colummns) len(seq_b), and high (rows) len(seq_a)
    table = [[float('inf')] * (len(seq_b) + 1) for _ in range(len(seq_a) + 1)]

    # Fill the first column of each row with 'a' indices
    for y in range(len(seq_a) + 1):
        table[y][0] = y
    # Fill the first row of each colummn with 'b' indices
    for x  in range(len(seq_b) + 1):
        table[0][x] = x

    # Fill the table row by row with the minimum value possible for each node
    for y in range(1, len(seq_a) + 1):
        for x in range(1, len(seq_b) + 1):
            if seq_a[y - 1] == seq_b[x - 1]: # indices start in 0 not in 1
                diff = 0 # Match
            else:
                diff = 1 # Mismatch
            # Deletion, Insertion, either Match(1) or Mismatch(0)
            table[y][x] = min(table[y - 1][x] + 1, table[y][x - 1] + 1, table[y - 1][x - 1] + diff)

    return table[len(seq_a)][len(seq_b)] # Node with optimal alignment (Lower right corner)

if __name__ == "__main__":
    print(edit_distance(input(), input()))
