#Uses python3
import sys

def max_dot_product(seq_a, seq_b):
    '''Given two sequences 𝑎1, 𝑎2, . . . , 𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad)
    and 𝑏1, 𝑏2, . . . , 𝑏𝑛 (𝑏𝑖 is the average number of clicks per day of the 𝑖-th slot),
    we need to partition them into 𝑛 pairs (𝑎𝑖, 𝑏𝑗 )
    such that the sum of their products is maximized.'''

    res = 0
    for _ in range(len(seq_a)):
        index_a = seq_a.index(max(seq_a))#The largest number of a
        index_b = seq_b.index(max(seq_b))#The largest number of b
        res += seq_a[index_a] * seq_b[index_b]#The sum of a * b
        seq_a.pop(index_a)#Delete number from a
        seq_b.pop(index_b)#Delete number from b
    return res

if __name__ == '__main__':
    numbers = sys.stdin.read()
    data = list(map(int, numbers.split()))
    n = data[0]
    nums_a = data[1:(n + 1)]
    nums_b = data[(n + 1):]
    print(max_dot_product(nums_a, nums_b))
