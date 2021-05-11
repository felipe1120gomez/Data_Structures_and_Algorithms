# python3

from collections import namedtuple
from collections import deque
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs, n_jobs):
    '''Given a number of threads, and a deque (list) of jobs.
    It determines which thread does the job and when it starts.'''

    result = list()
    # 2D table [0, id], 0 will serve to carry the sum of the time, id is the thread
    next_free_time = [[0, id] for id in range(0, n_workers)]
    # heapq is used to get the thread with the least time, if there are two with the same time,
    # returns the one with the smallest id
    heapq.heapify(next_free_time)
    for job in range(n_jobs):
        thread = heapq.heappop(next_free_time) # Thread that will receive the job
        result.append(AssignedJob(thread[1], thread[0])) # Thread id and job start time
        # Take the work from the deque and add it to the existing time in that thread
        thread[0] += jobs.popleft()
        heapq.heappush(next_free_time, thread) # Push the updated thread to the heapq

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    # We use deque to get the first element (index 0) in O(1)
    jobs = deque(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs, n_jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
