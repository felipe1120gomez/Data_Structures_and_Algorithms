# Paths in Graphs

## bfs.py

This program, given an undirected graph with 𝑛 vertices and 𝑚 edges and two vertices 𝑢 and 𝑣, computes the length of the shortest path between 𝑢 and 𝑣 (that is, the minimum number of edges in a path from 𝑢 to 𝑣).
* Sample.
```
Input: 4 4
       1 2
       4 1
       2 3
       3 1
       2 4

```
* Output: 2

There is a unique shortest path between vertices 2 and 4 in this graph: 2 − 1 − 4.

## bipartite.py

An undirected graph is called bipartite if its vertices can be split into two parts such that each edge of the graph joins two vertices from different parts. Bipartite graphs arise naturally in applications where a graph is used to model connections between objects of two different types (say, boys and girls; or students and dormitories).

An alternative definition is the following: a graph is bipartite if its vertices can be colored with two colors (say, black and white) such that the endpoints of each edge have different colors.

Given an undirected graph with 𝑛 vertices and 𝑚 edges, check whether it is bipartite.
* Sample.
```
Input: 4 4
       1 2
       4 1
       2 3
       3 1

```
* Output: 0

This graph is not bipartite. To see this assume that vertex 1 is colored white. Then the vertices 2 and 3 should be colored black since the graph contains the edges {1, 2} and {1, 3}. But then the edge {2, 3} has both endpoints of the same color.


## dijkstra.py

This program, given a directed graph with positive edge weights and with 𝑛 vertices and 𝑚 edges as well as two vertices 𝑢 and 𝑣, compute the weight of the shortest path between 𝑢 and 𝑣 (that is, the minimum total weight of a path from 𝑢 to 𝑣).
* Sample.
```
Input: 4 4
       1 2 1
       4 1 2
       2 3 2
       1 3 5
       1 3

```
```
Output: 3

```
There is a unique shortest path from vertex 1 to vertex 3 in this graph (1 → 2 → 3), and it has a weight of 3.


## negative_cycle.py

This program, given a directed graph with possibly negative edge weights and with 𝑛 vertices and 𝑚 edges, check whether it contains a cycle of negative weight.
* Sample.
```
Input: 4 4
       1 2 -5
       4 1 2
       2 3 2
       3 1 1

```
```
Output: 1

```
The weight of cycle 1 → 2 → 3 is equal to −2, that is, negative.


## shortest_paths.py

This program, given a directed graph with possibly negative edge weights and with 𝑛 vertices and 𝑚 edges as well as its vertex 𝑠, compute the length of shortest paths from 𝑠 to all other vertices of the graph.
* Sample.
```
Input: 5 4
       1 2 1
       4 1 2
       2 3 2
       3 1 -5
       4

```
```
Output: -
        -
        -
        0
        *

```
In this case, the distance from 4 to vertices 1, 2, and 3 is −∞ since there is a negative cycle 1 → 2 → 3 that is reachable from 4. The distance from 4 to 4 is zero. There is no path from 4 to 5.
