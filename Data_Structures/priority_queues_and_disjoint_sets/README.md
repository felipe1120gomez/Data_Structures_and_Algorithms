# Priority Queues and Disjoint Sets

## build_heap.py

Make a heap by applying a certain number of swaps to the array. Swap is an operation that exchanges elements 𝑎𝑖 and 𝑎𝑗 of the array 𝑎 for some 𝑖 and 𝑗. This script converts the array into a heap using only 𝑂(𝑛) swaps. Note that we are looking for a min-heap instead of a max-heap in this case.
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
* After swapping elements 5 in position 1 and 2 in position 3 the array becomes 1 2 3 5 4, which is already a heap, because 𝑎0 = 1 < 2 = 𝑎1, 𝑎0 = 1 < 3 = 𝑎2, 𝑎1 = 2 < 5 = 𝑎3, 𝑎1 = 2 < 4 = 𝑎4.

## job_queue.py

This program is parallelized and uses 𝑛 independent threads to process the given list of 𝑚 jobs. Threads take jobs in the order they are given in the input. If there is a free thread, it immediately takes the next job from the list. If a thread has started processing a job, it doesn’t interrupt or stop until it finishes processing the job. If several threads try to take jobs from the list simultaneously, the thread with a smaller index takes the job. For each job, you know exactly how long will it take any thread to process this job, and this time is the same for all the threads.
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

Task. There are 𝑛 tables stored in one database. The tables are numbered from 1 to 𝑛. All tables share the same set of columns. Each table contains either several rows with real data or a symbolic link to another table. Initially, all tables contain data, and 𝑖-th table has 𝑟𝑖 rows. You need to perform 𝑚 of the following operations:

1. Consider table number 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖. Traverse the path of symbolic links to get to the data. That is, while 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 contains a symbolic link instead of real data do 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ← symlink(𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖)
2. Consider the table number 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 and traverse the path of symbolic links from it in the same manner as for 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖.
3. Now, 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 and 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 are the numbers of two tables with real data. If 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ̸= 𝑠𝑜𝑢𝑟𝑐𝑒𝑖, copy all the rows from table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 to table 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖, then clear the table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 and instead of real data put a symbolic link to 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 into it.
4. Print the maximum size among all 𝑛 tables (recall that size is the number of rows in the table). If the table contains only a symbolic link, its size is considered to be 0.
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
4. Traversing the path of symbolic links from 4 we have 4 → 2 → 1, and the path from 5 is 5 → 3. So we are actually merging tables 3 and 1. We copy all the rows from table number 1 into table number 3, and now table number 3 has 5 rows of data, which is the new maximum.
5. All tables now directly or indirectly point to table 3, so all other merges won’t change anything.
