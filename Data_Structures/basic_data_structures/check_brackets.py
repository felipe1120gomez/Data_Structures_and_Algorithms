# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    '''Check that both characters match.'''

    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    '''Check that the brackets are used correctly,
    otherwise it returns the index where the error is.'''

    opening_brackets_stack = list()
    for i, char in enumerate(text):
        if char in "([{":
            opening_brackets_stack.append(Bracket(char, i))

        if char in ")]}":
            if not opening_brackets_stack: # If there is nothing in the list
                return i + 1

            top = opening_brackets_stack.pop() # Comparison
            if not are_matching(top.char, char):
                return i + 1

    if opening_brackets_stack: # If there is anything left on the list
        top = opening_brackets_stack.pop()
        return top.position + 1


    return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
