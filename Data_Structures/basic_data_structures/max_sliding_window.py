# python3

from collections import deque

def max_sliding_window(sequence, size):
    '''Given a sequence of numbers and a window size,
    returning the largest number among the numbers in the window,
    the window will go through the entire sequence.'''

    window = deque()
    max_nums = list()
    length = len(sequence)
    for index in range(length):

        # Keep only relevant numbers
        # If the last number in the window is less than the one to be entered, it is eliminated
        while window and sequence[index] >= sequence[window[-1]]:
            window.pop()
        window.append(index) # When all the minor numbers are eliminated we add the following

        # The number at index 0 is already outside the window
        if index >= size and window and window[0] == index - size:
            window.popleft() # We remove the number for being outside the window

        # The window must move and we must select the maximum number
        if index >= size - 1:
            max_nums.append(sequence[window[0]])

    return max_nums


if __name__ == '__main__':
    number = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == number
    window_size = int(input())
    print(*max_sliding_window(input_sequence, window_size))
