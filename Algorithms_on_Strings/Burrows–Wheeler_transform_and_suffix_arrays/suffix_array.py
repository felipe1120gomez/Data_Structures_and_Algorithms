# python3

def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """

    len_text = len(text)

    # pair [suffix, index]
    suffix_array = [[text[suf_index:], suf_index] for suf_index in range(len_text)]

    suffix_array = sorted(suffix_array)

    result = [suf_index[1] for suf_index in suffix_array]

    return result


if __name__ == '__main__':
    in_text = input().strip()
    print(" ".join(map(str, build_suffix_array(in_text))))
