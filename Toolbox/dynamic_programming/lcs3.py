#Uses python3

import sys

def lcs3(seq_a, seq_b, seq_c):
    '''Compute the length of a longest common subsequence of three sequences.'''

    # 3D table of depth len(seq_c), wide len(seq_b), and high len(seq_a)
    table = [[[0] * (len(seq_c) + 1) for _ in range(len(seq_b) + 1)] for _ in range(len(seq_a) + 1)]

    # Fill the table
    for y in range(1, len(seq_a) + 1):
        for x in range(1, len(seq_b) + 1):
            for z in range(1, len(seq_c) + 1):
                # Match
                if seq_a[y - 1] == seq_b[x - 1] == seq_c[z - 1]: # Indexes start in 0 not in 1
                    table[y][x][z] = table[y - 1][x - 1][z - 1] + 1
                # Mismatch
                else:
                    table[y][x][z] = max(max(table[y - 1][x][z], table[y][x - 1][z]), table[y][x][z - 1])

    return max(max(map(max, table))) # Max value in all table

if __name__ == '__main__':
    numbers = sys.stdin.read()
    data = list(map(int, numbers.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
