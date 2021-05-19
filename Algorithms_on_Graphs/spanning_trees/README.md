# Minimum Spanning Trees

## connecting_points.py

This program, given 𝑛 points on a plane, connect them with segments of minimum total length such that there is a path between any two points.
* Sample.
```
Input: 5
       0 0
       0 2
       1 1
       3 0
       3 2


```
* Output: 7.064495102

The total length here is equal to 2√2 + √5 + 2

## clustering.py

Clustering is a fundamental problem in data mining. The goal is to partition a given set of objects into subsets (or clusters) in such a way that any two objects from the same subset are close (or similar) to each other, while any two objects from different subsets are far apart.

Given 𝑛 points on a plane and an integer 𝑘, compute the largest possible value of 𝑑 such that the given points can be partitioned into 𝑘 non-empty subsets in such a way that the distance between any two points from different subsets is at least 𝑑.
* Sample.
```
Input: 8
       3 1
       1 2
       4 6
       9 8
       9 9
       8 9
       3 11
       4 12
       4

```
* Output: 5.000000000
