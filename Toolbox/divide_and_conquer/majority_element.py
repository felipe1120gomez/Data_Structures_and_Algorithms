# Uses python3
import sys

def get_majority_element(nums, left, right):
    '''Given the middle of the list count the occurrences of each number,
    it returns a dictionary with the result.'''

    targets = dict()

    # check array on zero elements
    if left == right:
        return targets

    # check array on only one element
    if left + 1 == right:
        targets[nums[left]] = 1
        return targets

    # sort the array to get n*log(n) complexity
    nums.sort()

    # initialize counters
    cur_elem = nums[left]
    cur_cnt = 0
    targets = dict()

    # iterate through sorted array
    for i in range(left, right):

        if nums[i] == cur_elem:
            cur_cnt += 1

        else:
            if cur_cnt > len(a) // 2:# The number is already a majority.
                return False
                break
            targets[cur_elem] = cur_cnt
            cur_elem = nums[i] # next number
            cur_cnt = 1 # already one

    # last element check
    if cur_cnt > len(nums) // 2:# The number is already a majority.
        return False

    targets[cur_elem] = cur_cnt

    return targets

# divide-and-conqurer algorithm
# n*log(n) complexity
# T(n) = 2*T(n/2) + Teta(n)
def get_majority_element_div(nums, left, right):
    '''Check whether an input sequence contains a majority element.'''

    # check array of zero elements
    if len(nums) == 0:
        return -1

    # check array of one element
    elif len(nums) == 1:
        return -1

    else:
        # split point
        mid = len(nums) // 2

        mid_l = get_majority_element(nums, left, mid)
        mid_r = get_majority_element(nums, mid, right)

        if not mid_l or not mid_r:
            return 1
        # sum of a number in both halfs is majority?
        for key in mid_l.keys():
            if key in mid_r.keys():
                if mid_l[key] + mid_r[key] > mid:
                    return 1

        return -1

if __name__ == '__main__':
    numbers = sys.stdin.read()
    n, *a = list(map(int, numbers.split()))
    if get_majority_element_div(a, 0, n) != -1:
        print(1)
    else:
        print(0)
