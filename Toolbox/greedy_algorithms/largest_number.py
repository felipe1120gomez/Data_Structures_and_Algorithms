#Uses python3

import sys

def max_combination(max_num, num):
    '''Select the best possible combination of two numbers.'''

    first = str(max_num) + str(num)
    second = str(num) + str(max_num)

    if int(first) > int(second):#If it is better for max_num(max_digit) to stay ahead
        return False # max_num is not changed
    elif int(first) < int(second):#If it is better that num(digit) stay ahead
        return True # max_num is changed

def largest_number(nums):
    '''Compose the largest number out of a set of integers.'''

    answer = str()
    while nums:
        max_digit = None
        for digit in nums:
            if max_digit is None:
                max_digit = digit
                continue
            elif len(str(max_digit)) == len(str(digit)):#If the numbers have the same number of digits
                if digit > max_digit: # The largest is chosen
                    max_digit = digit
                    continue
            elif len(str(max_digit)) != len(str(digit)):#If the numbers have different amount of digits
                if max_combination(max_digit, digit):#The best possible combination is chosen
                    max_digit = digit
                    continue

        answer += str(max_digit)
        nums.remove(max_digit)

    return int(answer)

if __name__ == '__main__':
    numbers = sys.stdin.read()
    data = numbers.split()
    a = data[1:]
    print(largest_number(a))
