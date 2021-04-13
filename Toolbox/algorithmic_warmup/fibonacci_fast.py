# Uses python3

def calc_fib(number):
    '''Given an integer n, find the nth Fibonacci number Fn.'''
    if number <= 1:
        return number

    previous = 0
    current  = 1

    for _ in range(number - 1):
        previous, current = current, previous + current

    return current

if __name__ == '__main__':
    num = int(input())
    print(calc_fib(num))
