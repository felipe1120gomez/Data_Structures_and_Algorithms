# python3

class Equation:
    """
    A class to represent a matrix of equations.

    ...

    Attributes
    ----------
    expression : list()
        Left side of the equation
    term : list()
        Right side of the equation

    Methods
    -------

    """

    def __init__(self, left_s, right_s):
        self.expression = left_s
        self.term = right_s

class Position:
    """
    A class to represent a pivot row.

    ...

    Attributes
    ----------
    row : int()
        Row of the pivot
    col : int()
        Column of the pivot

    Methods
    -------

    """

    def __init__(self, row, col):
        self.row = row
        self.col = col


def select_pivot_element(pivot, equ_express, used_rows):
    '''Select the next equation (row) that has not been reduced'''

    while used_rows[pivot.row] or equ_express[pivot.row][pivot.col] == 0:
        pivot.row += 1

    return pivot

def swap_lines(equ_express, equ_term, used_rows, pivot):
    '''Swap row to top of non-pivot rows'''

    equ_express[pivot.col], equ_express[pivot.row] = equ_express[pivot.row], equ_express[pivot.col]
    equ_term[pivot.col], equ_term[pivot.row] = equ_term[pivot.row], equ_term[pivot.col]
    used_rows[pivot.col], used_rows[pivot.row] = used_rows[pivot.row], used_rows[pivot.col]
    pivot.row = pivot.col

def process_pivot_element(equ_express, equ_term, pivot, used_rows):
    '''Gaussian Elimination, Row Reduction'''

    size = len(equ_express)
    scale = equ_express[pivot.row][pivot.col]

    # scaling the row
    if scale != 1:

        for column in range(size):
            equ_express[pivot.row][column] /= scale
        equ_term[pivot.row] /= scale

    # reduce rows except pivot
    for row in range(size):

        if row != pivot.row:
            multiple = equ_express[row][pivot.col]

            for column in range(size):
                equ_express[row][column] -= equ_express[pivot.row][column] * multiple
            equ_term[row] -= equ_term[pivot.row] * multiple

    used_rows[pivot.row] = True

def solve_equation(equation):
    '''Solve a system of equations by Gaussian elimination'''

    equ_express = equation.expression
    equ_term = equation.term
    size = len(equ_express)
    used_rows = [False] * size

    for column in range(size):
        pivot = Position(0, column)
        pivot = select_pivot_element(pivot, equ_express, used_rows)
        swap_lines(equ_express, equ_term, used_rows, pivot)
        process_pivot_element(equ_express, equ_term, pivot, used_rows)

    return equ_term


if __name__ == '__main__':
    num_equ = int(input())
    left_side = []
    right_side = []

    for _ in range(num_equ):
        line = list(map(float, input().split()))
        left_side.append(line[:num_equ])
        right_side.append(line[num_equ])
    matrix = Equation(left_side, right_side)

    term_column = solve_equation(matrix)
    for res in term_column:
        print("%.20lf" % res)
