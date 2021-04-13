# Uses python3

def get_fib(num):
    '''Given an integer n, find the nth Fibonacci number Fn.'''
    if num <= 1:
        return num

    num = num % 60
    previous = 0
    current  = 1

    for _ in range(num + 1):
        previous, current = current, previous + current

    return previous

def fibonacci_squares_fast(num):
    '''Given an integer n, find the last digit of
    the sum of squares of Fibonacci numbers'''
    if num <= 1:
        return num
    # F(n + 1 ) - 1
    n_fib = num
    num = (num + 1) % 60 # The Fibonacci series has a 60 digit cycle.
    previous = 0
    current  = 1

    for _ in range(num - 1):
        previous, current = current, previous + current

    return (previous * get_fib(n_fib)) % 10
    # F0^2 + F1^2 + ⋯ + Fn^2 = Fn+1 * Fn.

if __name__ == '__main__':
    number = int(input())
    print(fibonacci_squares_fast(number))
