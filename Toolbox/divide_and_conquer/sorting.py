# Uses python3
import sys
import random

def partition3(nums, left, right):
    '''3-way partition. partition the array into three parts: < 𝑥 part, = 𝑥 part, and > 𝑥 part.'''

    pivot = nums[left]
    next_l = left
    next_r = right
    i = next_l

    while i <= next_r :
        if nums[i] < pivot:
            nums[next_l], nums[i] = nums[i], nums[next_l] # Move the smaller number to left.
            next_l += 1 # The start of the list moves to right

        elif nums[i] > pivot:
            nums[next_r], nums[i] = nums[i], nums[next_r] # Move the largest number to right.
            next_r -= 1 # The end of the list moves to left
            i -= 1 # remain in the same i in this case
        i += 1
    return next_l, next_r

#def partition2(a, l, r):
    #x = a[l]
    #j = l
    #for i in range(l + 1, r + 1):
        #if a[i] <= x:
            #j += 1
            #a[i], a[j] = a[j], a[i]
    #a[l], a[j] = a[j], a[l]
    #return j

def randomized_quick_sort(nums, left, right):
    '''Random pivot quick sort algorithm'''

    if left >= right:
        return
    pivot = random.randint(left, right)
    nums[left], nums[pivot] = nums[pivot], nums[left]
    #use partition3
    mid_l, mid_r = partition3(nums, left, right)
    randomized_quick_sort(nums, left, mid_r - 1)
    randomized_quick_sort(nums, mid_l + 1, right)

if __name__ == '__main__':
    numbers = sys.stdin.read()
    n, *a = list(map(int, numbers.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
