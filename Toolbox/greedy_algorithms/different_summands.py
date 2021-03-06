# Uses python3
import sys

def optimal_summands(num):
    '''represent a given positive integer π as a sum of as many pairwise
    distinct positive integers as possible. That is, to find the maximum π such that π can be written as
    π1 + π2 + Β· Β· Β· + ππ where π1, . . . , ππ are positive integers and ππ ΜΈ= ππ for all 1 β€ π < π β€ π.'''

    summands = []
    temp_sum = 0

    for number in range(1, num + 1):
        temp_sum += number # Partial sum
        if temp_sum <= num:
            summands.append(number)

        else:
            temp_sum -= number
            prev = summands.pop() # Remove problematic number
            temp_sum -= prev
            last = num - temp_sum # ππ number
            summands.append(last)
            break

    return summands

if __name__ == '__main__':
    number = sys.stdin.read()
    n = int(number)
    opt_summands = optimal_summands(n)
    print(len(opt_summands))
    print(*opt_summands)
