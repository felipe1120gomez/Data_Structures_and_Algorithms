# Uses python3

def fibonacci_partial_sum_fast(start,  end):
    '''Given two non-negative integers m and n, where m <= n,
    find the last digit of the sum Fm + Fm+1 + · · · + Fn.'''

    start = start % 60
    end = end % 60
    total = 0
    current = 0
    next_n = 1

    if end < start:
        end += 60

    for j in range(end + 1):
        if j >= start:
            total += current % 60

        current, next_n = next_n, current + next_n

    return total % 10

if __name__ == '__main__':
    numbers = input()
    m, n = map(int, numbers.split())
    print(fibonacci_partial_sum_fast(m, n))
