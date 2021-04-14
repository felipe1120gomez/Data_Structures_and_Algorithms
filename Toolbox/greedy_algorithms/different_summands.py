# Uses python3
import sys

def optimal_summands(num):
    '''represent a given positive integer 𝑛 as a sum of as many pairwise
    distinct positive integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can be written as
    𝑎1 + 𝑎2 + · · · + 𝑎𝑘 where 𝑎1, . . . , 𝑎𝑘 are positive integers and 𝑎𝑖 ̸= 𝑎𝑗 for all 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.'''

    summands = []
    # Mathematical operation to find the first numbers
    sequence = int(((((num * 8) + 1) ** 0.5) - 1) / 2)
    # Mathematical operation to find the last number
    last_num = int(num - (((sequence - 1) * sequence) / 2))

    for i in range(1, sequence):
        summands.append(i)

    summands.append(last_num)

    return summands

if __name__ == '__main__':
    number = sys.stdin.read()
    n = int(number)
    opt_summands = optimal_summands(n)
    print(len(opt_summands))
    print(*opt_summands)
