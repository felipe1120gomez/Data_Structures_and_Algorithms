# Python3 program to calculate
# Fibonacci no. modulo m using
# Pisano Period

# Calculate and return Pisano Period
# The length of a Pisano Period for
# a given m ranges from 3 to m * m
def pisano_period(mod):
    '''Is the period with which the sequence of
    Fibonacci numbers taken modulo m repeats.'''
    previous = 0
    current = 1
    for i in range(0, mod * mod):
        previous, current = current, (previous + current) % mod

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

# Calculate Fn mod m
def get_fibonacci_huge_fast(num, mod):
    '''Given two integers n and m, output Fn mod m
    (that is, the remainder of Fn when divided by m).'''

    pisano = pisano_period(mod)

    num = num % pisano

    previous = 0
    current = 1

    if num <= 1:
        return num
        
    for _ in range(num - 1):
        previous, current = current, previous + current

    return current % mod

if __name__ == '__main__':
    numbers = input()
    num_1, mod_1 = map(int, numbers.split())
    print(get_fibonacci_huge_fast(num_1, mod_1))
