# Uses python3

def get_change(num):
    '''find the minimum number of coins needed to change the
    input value (an integer) into coins with denominations 1, 5, and 10.'''
    #This is not an optimal algorithm.

    if num in (1, 5, 10):
        return 1

    change = 0
    count = 0
    while change < num:
        if (change + 10) <= num:
            change += 10
            count += 1
        elif (change + 5) <= num:
            change += 5
            count += 1
        elif (change + 1) <= num:
            change += 1
            count += 1

    return count

if __name__ == '__main__':
    number = int(input())
    print(get_change(number))
