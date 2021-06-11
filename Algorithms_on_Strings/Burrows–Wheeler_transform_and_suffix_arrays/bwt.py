# python3

def burrows_wheeler_transform(text):
    '''Construct the Burrows–Wheeler transform of a string'''

    len_text = len(text)

    matrix = [None] * len_text

    result = str()

    text = list(text)

    for index in range(len_text):
        new_head = text[-1]
        new_head = list(new_head)
        rotation = new_head + text[:-1] # put the last symbol ahead
        str_rotation = ''.join(rotation)
        matrix[index] = str_rotation
        text = rotation

    matrix.sort()

    for string in matrix:
        result += string[-1]

    return result


if __name__ == '__main__':
    in_text = input().strip()
    print(burrows_wheeler_transform(in_text))
