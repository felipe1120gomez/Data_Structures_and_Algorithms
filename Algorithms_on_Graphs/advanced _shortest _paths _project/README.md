# Advanced Shortest Paths

## friend_suggestion.py

This script computes the distance between several pairs of nodes in the graph using a bidirectional Dijkstra algorithm.
* Sample.
```
Input: 4 4
       1 2 1
       4 1 2
       2 3 2
       1 3 5
       1
       1 3

```
* Output: 3

There is a direct edge from node 1 to node 3 of length 5, but there is a shorter path 1 → 2 → 3 of length 1 + 2 = 3.

## dist_with_coords.py

This script computes the distance between several pairs of nodes in the graph faster using coordinates with an A* algorithm.
* Sample.
```
Input: 4 4
       0 0
       0 1
       2 1
       2 0
       1 2 1
       4 1 2
       2 3 2
       1 3 6
       1
       1 3

```
* Output: 3

There is a direct edge from node 1 to node 3 of length 6, but there is a shorter path 1 → 2 → 3 of length 1 + 2 = 3.

## dist_with_coords_bidirec.py

This script computes the distance between several pairs of nodes in the graph faster using coordinates with a bidirectional A* algorithm.
* Sample.
```
Input: 4 4
       0 0
       0 1
       2 1
       2 0
       1 2 1
       4 1 2
       2 3 2
       1 3 6
       1
       1 3

```
* Output: 3

There is a direct edge from node 1 to node 3 of length 6, but there is a shorter path 1 → 2 → 3 of length 1 + 2 = 3.
