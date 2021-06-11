# python3

def sort_characters(text):
    num_sym = 91 # ascii to Z

    len_text = len(text)

    order = [None] * len_text

    count = [0] * num_sym

    for index in range(len_text):
        count[ord(text[index])] = count[ord(text[index])] + 1

    for p_sum in range(1, num_sym):
        count[p_sum] = count[p_sum] + count[p_sum - 1]

    for index in range(len_text - 1, -1, - 1):
        char = ord(text[index])

        count[char] = count[char] - 1

        order[count[char]] = index

    return order


def compute_char_classes(text, order):
    len_text = len(text)

    char_class  = [None] * len_text

    char_class[order[0]] = 0

    for index in range(1, len_text):
        if text[order[index]] != text[order[index - 1]]:
            char_class[order[index]] = char_class[order[index - 1]] + 1

        else:
            char_class[order[index]] = char_class[order[index - 1]]

    return char_class


def sort_double(text, length, order, char_class):
    len_text = len(text)

    new_order = [None] * len_text

    count = [0] * len_text

    for index in range(len_text):
        count[char_class[index]] = count[char_class[index]] + 1

    for p_sum in range(1, len_text):
        count[p_sum] = count[p_sum] + count[p_sum - 1]

    for index in range(len_text - 1, -1, - 1):
        start_char = (order[index] - length + len_text) % len_text

        cur_class = char_class[start_char]

        count[cur_class] = count[cur_class] - 1

        new_order[count[cur_class]] = start_char

    return new_order


def update_classes(order, char_class, length):
    len_order = len(order)

    new_class = [None] * len_order

    new_class[order[0]] = 0

    for index in range(1, len_order):
        cur = order[index]

        prev = order[index - 1]

        mid = (cur + length) % len_order

        mid_prev = (prev + length) % len_order

        if char_class[cur] != char_class[prev] or char_class[mid] != char_class[mid_prev]:
            new_class[cur] = new_class[prev] + 1

        else:
            new_class[cur] = new_class[prev]

    return new_class


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """

    # sorting single charater
    order = sort_characters(text)

    char_class = compute_char_classes(text, order)

    length = 1

    # sort shifts of 2length
    while length < len(text):

        order = sort_double(text, length, order, char_class)

        char_class = update_classes(order, char_class, length)

        length = 2 * length

    return order


def pattern_matching(text, patt, suffix_array):
    '''Returns the indexes where the pattern starts in the text'''

    min_index = 0

    max_index = len(text) - 1

    # get start index
    # discard all suffixes less than the pattern
    while min_index <= max_index:
        mid_index = (min_index + max_index) // 2
        string = text[suffix_array[mid_index]:]

        if patt > string:
            min_index = mid_index + 1

        else:
            max_index = mid_index - 1

    start = min_index
    max_index = len(text) - 1

    # get end index
    # check if a string (suffix) starts with pattern
    while min_index <= max_index:
        mid_index = (min_index + max_index) // 2
        first = suffix_array[mid_index]
        last = suffix_array[mid_index] + len(patt)
        string = text[first:last]

        if string == patt:
            min_index = mid_index + 1

        else:
            max_index = mid_index - 1

    end = max_index

    if start > end:
        return []

    else:
        # The values between these two indices in the suffix array are
        # the indices in the text where the pattern starts
        return suffix_array[start:end + 1]


def find_occurrences(text, patterns):
    result = set()

    text = text + '$'

    # get suffix array
    suffix_array = build_suffix_array(text)

    for patt in patterns:
        match = pattern_matching(text, patt, suffix_array)
        for index in match:
            result.add(index)

    return result


if __name__ == '__main__':
    in_text = input().strip()
    pattern_count = int(input().strip())
    in_patterns = input().strip().split()
    occs = find_occurrences(in_text, in_patterns)
    print(" ".join(map(str, occs)))
