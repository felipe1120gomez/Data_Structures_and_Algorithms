# Divide and Conquer

These scripts use the sys module to read the input data.
Press ctrl z after entering the data to run the script.

## binary_search.py

Algorithm that allows searching very efficiently (even huge) lists, provided that the list is sorted.
* Sample.
```
Input: 5 1 5 8 12 13
       5 8 1 23 1 11
```
* Output: 2 0 -1 0 -1
* The first 5 are the length of each list, the first line is the list to search, the second line is the keys we seek.

## inversions.py

Algorithm to count the number of inversions of a given sequence.
* Sample.
```
Input: 5
       2 3 9 2 9
```
* Output: 2

The two inversions here are (1, 3) (𝑎1 = 3 > 2 = 𝑎3) and (2, 3) (𝑎2 = 9 > 2 = 𝑎3).
The first 5 is the length of the list.

## majority_element.py

Algorithm to check whether an input sequence contains a majority element.
* Sample.
```
Input: 4
       1 2 3 4
```       
* Output: 0

There is no majority element in this sequence.
The first 4 is the length of the list.

## points_and_segments.py

Given a set of points on a line and a set of segments on a line. The goal is to compute, for each point, the number of segments that contain this point.
* Sample.
```
Input: 2 3
       0 5
       7 10
       1 6 11
```
* Output: 1 0 0

Here, we have two segments and three points. The first point lies only in the first segment while the remaining two points are outside of all the given segments.
2 = number of segments, 3 = number of points.

## sorting.py

Randomized quick sort algorithm with a 3-way partition.
* Sample.
```
Input: 5
       2 3 9 2 2
```
* Output: 2 2 2 3 9
