# Uses python3

def fibonacci_sum_fast(num):
    '''Given an integer n, find the last
    digit of the sum F0 + F1 + · · · + Fn.'''
    if num <= 1:
        return num
    # S(n) = F(n + 2 ) - 1
    num = (num + 2) % 60 # The Fibonacci series has a 60 digit cycle.
    previous = 0
    current  = 1

    for _ in range(num - 1):
        previous, current = current, previous + current

    return (current - 1) % 10

if __name__ == '__main__':
    number = int(input())
    print(fibonacci_sum_fast(number))
