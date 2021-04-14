# Uses python3
def evalt(a, b, op):
    '''Given two numbers a and b, it returns the result
    of the mathematical operation op, between a and b.'''

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_max(i, j, op, m, M):
    '''Evaluates all possible mathematical operations
    and returns the minimum and maximum values.'''

    mmin = 10000 # High value to avoid picking it
    mmax = -10000 # Low value to avoid picking it
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        mmin = min(mmin, a, b, c, d)
        mmax = max(mmax, a, b, c, d)
    return(mmin, mmax)

def get_maximum_value(dataset):
    '''Return the maximum possible value of the given arithmetic expression
    among different orders of applying arithmetic operations.'''

    operations = dataset[1:len(dataset):2] # The elements are chosen in the indices 1, 3, 5 ....
    digits = dataset[0:len(dataset)+1:2] # The elements are chosen in the indices 0, 2, 4 ....
    n = len(digits)
    # 2D tables of wide (colummns) len(digits), and high (rows) len(digits)
    table_min = [[0 for i in range(n)] for j in range(n)] # Minimized values
    table_max = [[0 for i in range(n)] for j in range(n)] # Maximized values
    for i in range(n):
        table_min[i][i] = int(digits[i]) #So that the tables will look like
        table_max[i][i] = int(digits[i]) #[[i, 0, 0...], [0, i, 0...], [0, 0, i,...]]
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            table_min[i][j], table_max[i][j] = min_max(i,j,operations,table_min,table_max)
    return table_max[0][n - 1] # First row, last colummn

if __name__ == "__main__":
    print(get_maximum_value(input()))
