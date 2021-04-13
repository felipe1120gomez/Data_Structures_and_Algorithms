# Uses python3

def gcd_fast(num_a, num_b):
    '''Given two integers a and b, find their
    greatest common divisor using Euclid's algorithm.'''
    if num_b == 0:
        return num_a

    return gcd_fast(num_b, num_a % num_b)

if __name__ == "__main__":
    numbers = input()
    num_1, num_2 = map(int, numbers.split())
    print(gcd_fast(num_1, num_2))
