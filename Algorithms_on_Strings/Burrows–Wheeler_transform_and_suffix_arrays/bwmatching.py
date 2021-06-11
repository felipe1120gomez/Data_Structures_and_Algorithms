# python3

def preprocess_bwt(bwt):
    """
    Preprocess the Burrows-Wheeler Transform bwt of some text
    and compute as a result:
      * starts - for each character C in bwt, starts[C] is the first position
          of this character in the sorted array of
          all characters of the text.
      * occurs - for each character C in bwt and each position P in bwt,
          occ_count_before[C][P] is the number of occurrences of character C in bwt
          from position 0 to position P inclusive.
    """

    len_bwt = len(bwt)

    last_column = list(bwt)

    first_column = sorted(last_column)

    starts = dict()

    chars = ['A', 'C', 'G', 'T', '$']

    occurs = {symbol: [0 for _ in range(len_bwt + 1)] for symbol in chars}

    for index in range(len_bwt):
        sybmol_f = first_column[index]
        symbol_l = last_column[index]

        if sybmol_f not in starts:
            starts[sybmol_f] = index

        for symbol in occurs.keys():

            if symbol == symbol_l:
                # The previous sum plus one
                occurs[symbol_l][index + 1] = occurs.get(symbol_l)[index] + 1
            else:
                # Move the sum of the other symbols one index forward
                occurs[symbol][index + 1] = occurs.get(symbol)[index]

    return starts, occurs


def count_occurrences(pattern, bwt, starts, counts):
    """
    Compute the number of occurrences of string pattern in the text
    given only Burrows-Wheeler Transform bwt of the text and additional
    information we get from the preprocessing stage - starts and counts.
    """

    len_bwt = len(bwt)

    pattern = list(pattern)

    top = 0

    bottom = len_bwt

    while top <= bottom:

        if pattern:
            symbol = pattern.pop()

            # if positions from top to bottom in LastColumn contain an occurrence of symbol:
            if counts.get(symbol)[top] != 0 or counts.get(symbol)[bottom] != 0:
                top = starts.get(symbol) + counts.get(symbol)[top]
                bottom = starts.get(symbol) + counts.get(symbol)[bottom]
            else:
                return 0

        else:
            return bottom - top


if __name__ == '__main__':
    in_bwt = input().strip()
    pattern_count = int(input().strip())
    patterns = input().strip().split()
    # Preprocess the BWT once to get starts and occ_count_before.
    # For each pattern, we will then use these precomputed values and
    # spend only O(|pattern|) to find all occurrences of the pattern
    # in the text instead of O(|pattern| + |text|).
    starts_ind, occ_counts_before = preprocess_bwt(in_bwt)
    for patt in patterns:
        result = count_occurrences(patt, in_bwt, starts_ind, occ_counts_before)
        print(result, sep=' ', end=' ', flush=True)
