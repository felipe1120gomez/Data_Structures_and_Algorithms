# Uses python3
import sys

def get_change(money):
    '''The minimum number of coins with denominations 1, 3, 4 that changes money.'''

    coins = [1, 3, 4]
    min_change = {0:0} # Store the values for each value from 0 to money

    for num in range(1, money + 1):
        min_change[num] = float('inf')# Set value to infinite

        for i in range(len(coins)):
            coin = coins[i]

            if num >= coin:
                prev_coin = num - coin
                num_coins = min_change[prev_coin] + 1

                if num_coins < min_change[num]:
                    min_change[num] = num_coins

    return min_change[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
