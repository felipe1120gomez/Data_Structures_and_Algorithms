# python3

def prefix_function(string):
    '''prefixs[i] is the length of the longest border of the prefix string[0:i]'''

    len_str = len(string)

    prefixs = [None for _ in range(len_str)]

    prefixs[0] = 0

    border = 0

    for index in range(1, len_str):

        # decrease border size
        while border > 0 and string[index] != string[border]:
            border = prefixs[border - 1]

        # increase border size
        if string[index] == string[border]:
            border += 1

        # mismatch
        else:
            border = 0

        prefixs[index] = border

    return prefixs


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text
    Knuth-Morris-Pratt Algorithm.
    """
    result = []

    len_pat = len(pattern)

    string = pattern + '$' + text

    prefixs = prefix_function(string)

    len_str = len(string)

    for index in range(len_pat + 1, len_str):

        # if the edge is equal to the length of the pattern
        # at that index the pattern ends in the text
        if prefixs[index] == len_pat:
            result.append(index - 2 * len_pat)

    return result


if __name__ == '__main__':
    in_pattern = input().strip()
    in_text = input().strip()
    occs = find_pattern(in_pattern, in_text)
    print(" ".join(map(str, occs)))
