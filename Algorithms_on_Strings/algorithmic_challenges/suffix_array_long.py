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


if __name__ == '__main__':
    in_text = input().strip()
    print(" ".join(map(str, build_suffix_array(in_text))))
