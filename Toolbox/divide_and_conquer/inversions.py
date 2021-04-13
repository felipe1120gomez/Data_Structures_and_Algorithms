# Uses python3
import sys

def sort_list(left, right):
    '''MergeSort(𝐴) returns a sorted array 𝐴 and the number of inversions in 𝐴.'''

    sort_a = list()
    count = 0

    while left and right:
        first_l = left[0]
        first_r = right[0]
        if first_l <= first_r:
            sort_a.append(first_l)
            left.remove(first_l)
        # An inversion is when the largest number is on the left,
        # and is moved to the bottom of the list.
        else:
            count += len(left)
            sort_a.append(first_r)
            right.remove(first_r)

    if len(left) > 0:
        sort_a.extend(left)
    if len(right) > 0:
        sort_a.extend(right)

    return sort_a, count

def get_number_of_inversions(array):
    '''Count the number of inversions of a given sequence.
    Merge(𝐵, 𝐶) returns the resulting sorted array
    and the number of pairs (𝑏, 𝑐) such that 𝑏 ∈ 𝐵, 𝑐 ∈ 𝐶, and 𝑏 > 𝑐'''

    if len(array) == 1:
        return array, 0

    mid = len(array) // 2

    mid_l = array[:mid]
    mid_r = array[mid:]

    m_lf, inv_lf = get_number_of_inversions(mid_l)
    m_rg, inv_rg = get_number_of_inversions(mid_r)
    sort_array, inversions = sort_list(m_lf, m_rg)

    return sort_array, (inv_lf + inv_rg + inversions)

if __name__ == '__main__':
    numbers = sys.stdin.read()
    n, *a = list(map(int, numbers.split()))
    n_inversions = get_number_of_inversions(a)[1]
    print(n_inversions)
