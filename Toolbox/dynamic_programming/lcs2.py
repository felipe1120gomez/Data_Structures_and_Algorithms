#Uses python3

import sys

def lcs2(seq_a, seq_b):
    '''Compute the length of a longest common subsequence of two sequences.'''

    # 2D table of wide (colummns) len(seq_a), and high (rows) len(seq_b)
    table = [[None] * (len(seq_a) + 1) for _ in range(len(seq_b) + 1)]

    # Fill first colummn of each row with 0
    for y in range(len(seq_b) + 1):
        table[y][0] = 0
    # Fill first row for all colummns with 0
    for x in range(len(seq_a) + 1):
        table[0][x] = 0

    # Fill the table row by row
    for y in range(1, len(seq_b) + 1):
        for x in range(1, len(seq_a) + 1):
            # Match
            if seq_a[x - 1] == seq_b[y - 1]: # Indexes start in 0 not in 1
                table[y][x] = table[y - 1][x - 1] + 1
            # Mismatch
            else:
                table[y][x] = max(table[y - 1][x], table[y][x - 1])

    return max(map(max, table)) # Max value in all table

if __name__ == '__main__':
    numbers = sys.stdin.read()
    data = list(map(int, numbers.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
