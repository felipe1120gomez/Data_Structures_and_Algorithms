# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    '''given a set of segments on a line mark as few points on a line as possible
    so that each segment contains at least one marked point.
    Sample:
    have three segments: [1, 3], [2, 5], [3, 6] (of length 2, 3, 3 respectively).
    All of them contain the point with coordinate 3: 1 ≤ 3 ≤ 3, 2 ≤ 3 ≤ 5, 3 ≤ 3 ≤ 6.'''

    points = list()
    for seg in segments:
        pairs = list()
        pairs.append(seg.start)
        pairs.append(seg.end)
        points.append(pairs)

    n_points = len(points)
    # Sort the list of tuples by
    # their second element.
    points.sort(key = lambda x: x[1])

    # To store the solution
    cordinates = []
    i = 0

    # Iterate over all the segments
    while i < n_points:

        cur_end = points[i][1] # End point current segment
        cordinates.append(cur_end)
        next_seg = i + 1 # Next segment

        if next_seg >= n_points:
            break

        next_str = points[next_seg][0] # Start point of next segment

        # Loop over all those segements whose
        # start point is less than the end
        # point of current segment
        while cur_end >= next_str:

            next_seg += 1 # Next segment
            if next_seg >= n_points:
                break
            next_str = points[next_seg][0] # Start point of next segment
        i = next_seg # Jump to the next segment

    return cordinates

if __name__ == '__main__':
    numbers = sys.stdin.read()
    l, *data = map(int, numbers.split())
    raw_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    opt_points = optimal_points(raw_segments)
    print(len(opt_points))
    print(*opt_points)
