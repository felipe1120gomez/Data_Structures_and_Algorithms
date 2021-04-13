# Uses python3

def get_fibonacci_last_digit_fast(number):
    '''Given an integer n, find the last digit of the nth
    Fibonacci number Fn (that is, Fn mod 10).'''
    if number <= 1:
        return number

    previous = 0
    current  = 1

    for _ in range(number - 1):
        previous, current = current % 10, (previous + current) % 10

    return current

if __name__ == '__main__':
    num = int(input())
    print(get_fibonacci_last_digit_fast(num))
