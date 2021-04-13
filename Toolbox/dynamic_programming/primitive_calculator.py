# Uses python3
import sys

def optimal_sequence(target):
    '''Given an integer n, compute the minimum number of operations
    (multiply n by 2, multiply n by 3, or add 1 to n)
    needed to obtain the number n starting from the number 1.'''

    cache = [0] * (target + 1)  # Reserve a cache for all the intermediate results

    # Loop an all the elements, checking for all the possible alternatives
    for i in range(1, len(cache)):
        cache[i] = cache[i-1] + 1
        if i % 2 == 0:
            cache[i] = min(cache[i], cache[i // 2] + 1)
        if i % 3 == 0:
            cache[i] = min(cache[i], cache[i // 3] + 1)

    result = [1] * cache[-1]  # List of length equal to the last item in the cache

    for i in range(1, cache[-1]):
        result[-i] = target  # Set the value in the rightmost index with the updated target value
        if cache[target-1] == cache[target] - 1:
            target -= 1
        elif target % 2 == 0 and (cache[target // 2] == cache[target] - 1):
            target //= 2
        else: # target % 3 == 0 and (cache[target // 3] == cache[target] - 1):
            target //= 3

    return result

number = sys.stdin.read()
n = int(number)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
