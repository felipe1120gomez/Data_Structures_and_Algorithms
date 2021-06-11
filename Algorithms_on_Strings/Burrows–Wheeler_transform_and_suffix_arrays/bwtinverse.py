# python3

def inverse_bwt(bwt):
    '''Reconstruct a string from its Burrows–Wheeler transform.'''

    len_bwt = len(bwt)

    result = [None] * len_bwt

    last_to_first_map = dict()

    last_column = [[bwt[i], i] for i in range(len_bwt)] # pair [symbol, id]

    first_column = sorted(last_column)

    for index in range(len_bwt):

        id_symbol = first_column[index][1]
        last_to_first_map[id_symbol] = index # map {id : index in first_column}

    # From last to first symbol

    ind_symbol = bwt.index('$')

    for index in range(len_bwt - 1, -1, -1):

        result[index] = bwt[ind_symbol]
        ind_symbol = last_to_first_map.get(ind_symbol)

    result = ''.join(result)

    return result


if __name__ == '__main__':
    in_bwt = input().strip()
    print(inverse_bwt(in_bwt))
