# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    '''Compute, for each point, the number of segments that contain this point.'''

    cnt = {}
    segments_num = 0

    # List of tuples (number, type)
    listpoints = [(x, 'start') for x in starts]
    listpoints += [(x, 'point') for x in points] # Extend listpoints
    listpoints += [(x, 'end') for x in ends] # Extend listpoints

    # Organize the list by numbers, regardless of type
    listpoints.sort()

    # The sum is preserved from one iteration to another, the new iteration modifies it
    for position, kind in listpoints:
        if kind == 'start': # Each segment adds 1
            segments_num += 1
        elif kind == 'end': # If it is outside the segment, subtract 1
            segments_num -= 1
        else:
            cnt[position] = segments_num # Add the point and its sum to the dictionary

    return [cnt[x] for x in points]

def naive_count_segments(starts, ends, points):
    '''Compute, for each point, the number of segments that contain this point.'''

    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    numbers = sys.stdin.read()
    data = list(map(int, numbers.split()))
    n = data[0]
    m = data[1]
    st = data[2:2 * n + 2:2]
    en   = data[3:2 * n + 2:2]
    pt = data[2 * n + 2:]
    #use fast_count_segments
    segm = fast_count_segments(st, en, pt)
    print(*segm)
