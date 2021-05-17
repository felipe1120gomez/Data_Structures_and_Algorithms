# Uses python3
import sys

def optimal_summands(num):
    '''represent a given positive integer 𝑛 as a sum of as many pairwise
    distinct positive integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can be written as
    𝑎1 + 𝑎2 + · · · + 𝑎𝑘 where 𝑎1, . . . , 𝑎𝑘 are positive integers and 𝑎𝑖 ̸= 𝑎𝑗 for all 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.'''

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
            last = num - temp_sum # 𝑎𝑘 number
            summands.append(last)
            break

    return summands

if __name__ == '__main__':
    number = sys.stdin.read()
    n = int(number)
    opt_summands = optimal_summands(n)
    print(len(opt_summands))
    print(*opt_summands)
