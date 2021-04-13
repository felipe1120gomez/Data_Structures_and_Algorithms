# Uses python3
import sys

def binary_search(nums, key):
    """Returns the index of key in the list if found, -1 otherwise.
    List must be sorted."""

    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == key:
            return middle
        elif nums[middle] > key:
            #Checking the left side
            right = middle - 1
        elif nums[middle] < key:
            #Checking the right side
            left = middle + 1
    return -1

if __name__ == '__main__':
    numbers = sys.stdin.read()
    data = list(map(int, numbers.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')
