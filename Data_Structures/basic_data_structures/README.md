# Basic Data Structures

## check_brackets.py

This script's first priority is to find the first unmatched closing bracket which either doesn’t have an opening bracket before it, like ] in ](), or closes the wrong opening bracket, like } in ()[}. If there are no such mistakes, then it should find the first unmatched opening bracket without the corresponding closing bracket after it, like ( in {}([]. If there are no mistakes, the script should inform the user that the usage of brackets is correct.
* Sample.
```
Input: foo(bar[i);
```
* Output: 10

) doesn’t match [, so ) is the first unmatched closing bracket, so we output its position, which is 10.

## tree_height.py

Given a description of a rooted tree. this script computes and outputs its height. Recall that the height of a (rooted) tree is the maximum depth of a node or the maximum distance from a leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.
* Sample.
```
Input: 5
       -1 0 4 0 3

```
* Output: 4

The input means that there are 5 nodes with numbers from 0 to 4, node 0 is the root, node 1 is a child of node 0, node 2 is a child of node 4, node 3 is a child of node 0, and node 4 is a child of node 3. The height of this tree is 4 because the number of nodes on the path from root 0 to leaf 2 is 4.

## process_packages.py

Given a series of incoming network packets this script simulates its processing. Packets arrive in some order. For each packet number 𝑖, you know the time when it arrived 𝐴𝑖 and the time it takes the processor to process it 𝑃𝑖 (both in milliseconds). There is only one processor, and it processes the incoming packets in the order of their arrival.
* Sample.
```
Input: 1 2
       0 1
       0 1

```
```
Output: 0
        - 1

```
The first packet arrived at time 0, the second packet also arrived at time 0 but was dropped, because the network buffer has size 1 and it was full with the first packet already. The first packet started processing at time 0, and the second packet was not processed at all.


## stack_with_max_naive.py

Stack is an abstract data type supporting the operations Push() and Pop(). It is not difficult to implement it in a way that both these operations work in constant time. This script implements a stack that also supports finding the maximum value and to ensure that all operations still work in constant time.
* Sample.
```
Input: 5
       push 1
       push 2
       max
       pop
       max
```
```
Output: 2
        1

```
After the first two push queries, the stack contains elements 1 and 2. After the pop query, element 2 is removed.

## max_sliding_window.py

Given a sequence 𝑎1, . . . , 𝑎𝑛 of integers and an integer 𝑚 ≤ 𝑛, find the maximum among {𝑎𝑖, . . . , 𝑎𝑖+𝑚−1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1.
* Sample.
```
Input: 8
       2 7 3 1 5 2 6 2
       4

```
* Output: 7 7 5 6 6

4 is the size of the window.
