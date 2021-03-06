# Priority Queues and Disjoint Sets

## build_heap.py

Make a heap by applying a certain number of swaps to the array. Swap is an operation that exchanges elements ππ and ππ of the array π for some π and π. This script converts the array into a heap using only π(π) swaps. Note that we are looking for a min-heap instead of a max-heap in this case.
* Sample.
```
Input: 5
       5 4 3 2 1

```
```
Output: 3
        1 4
        0 1
        1 3

```

* After swapping elements 4 in position 1 and 1 in position 4 the array becomes 5 1 3 2 4.
* After swapping elements 5 in position 0 and 1 in position 1 the array becomes 1 5 3 2 4
* After swapping elements 5 in position 1 and 2 in position 3 the array becomes 1 2 3 5 4, which is already a heap, because π0 = 1 < 2 = π1, π0 = 1 < 3 = π2, π1 = 2 < 5 = π3, π1 = 2 < 4 = π4.

## job_queue.py

This program is parallelized and uses π independent threads to process the given list of π jobs. Threads take jobs in the order they are given in the input. If there is a free thread, it immediately takes the next job from the list. If a thread has started processing a job, it doesnβt interrupt or stop until it finishes processing the job. If several threads try to take jobs from the list simultaneously, the thread with a smaller index takes the job. For each job, you know exactly how long will it take any thread to process this job, and this time is the same for all the threads.
* Sample.
```
Input: 2 5
       1 2 3 4 5

```
```
Output: 0 0
        1 0
        0 1
        1 2
        0 4

```

1. The two threads try to simultaneously take jobs from the list, so the thread with index 0 actually takes the first job and starts working on it at the moment 0.
2. The thread with index 1 takes the second job and starts working on it also at the moment 0.
3. After 1 second, thread 0 is done with the first job and takes the third job from the list, and starts processing it immediately at time 1.
4. One second later, thread 1 is done with the second job and takes the fourth job from the list, and starts processing it immediately at time 2.
5. Finally, after 2 more seconds, thread 0 is done with the third job and takes the fifth job from the list, and starts processing it immediately at time 4.

## merging_tables.py

Task. There are π tables stored in one database. The tables are numbered from 1 to π. All tables share the same set of columns. Each table contains either several rows with real data or a symbolic link to another table. Initially, all tables contain data, and π-th table has ππ rows. You need to perform π of the following operations:

1. Consider table number πππ π‘ππππ‘ππππ. Traverse the path of symbolic links to get to the data. That is, while πππ π‘ππππ‘ππππ contains a symbolic link instead of real data do πππ π‘ππππ‘ππππ β symlink(πππ π‘ππππ‘ππππ)
2. Consider the table number π ππ’ππππ and traverse the path of symbolic links from it in the same manner as for πππ π‘ππππ‘ππππ.
3. Now, πππ π‘ππππ‘ππππ and π ππ’ππππ are the numbers of two tables with real data. If πππ π‘ππππ‘ππππ ΜΈ= π ππ’ππππ, copy all the rows from table π ππ’ππππ to table πππ π‘ππππ‘ππππ, then clear the table π ππ’ππππ and instead of real data put a symbolic link to πππ π‘ππππ‘ππππ into it.
4. Print the maximum size among all π tables (recall that size is the number of rows in the table). If the table contains only a symbolic link, its size is considered to be 0.
* Sample.
```
Input: 5 5
       1 1 1 1 1
       3 5
       2 4
       1 4
       5 4
       5 3

```
```
Output: 2
        2
        3
        5
        5

```
In this sample, all the tables initially have exactly 1 row of data. Consider the merging operations:

1. All the data from table 5 is copied to table number 3. Table 5 now contains only a symbolic link to table 3, while table 3 has 2 rows. 2 becomes the new maximum size.
2. 2 and 4 are merged in the same way as 3 and 5.
3. We are trying to merge 1 and 4, but 4 has a symbolic link pointing to 2, so we actually copy all the data from table number 2 to table number 1, clear table number 2, and put a symbolic link to the table number 1 in it. Table 1 now has 3 rows of data, and 3 becomes the new maximum size.
4. Traversing the path of symbolic links from 4 we have 4 β 2 β 1, and the path from 5 is 5 β 3. So we are actually merging tables 3 and 1. We copy all the rows from table number 1 into table number 3, and now table number 3 has 5 rows of data, which is the new maximum.
5. All tables now directly or indirectly point to table 3, so all other merges wonβt change anything.
