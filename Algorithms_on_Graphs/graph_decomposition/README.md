# Graph Decomposition

## reachability.py

This script represents a maze as an undirected graph: vertices of the graph are cells of the maze, two vertices are connected by an undirected edge if they are adjacent and there is no wall between them. Then, to check whether there is a path between two given cells in the maze, it suffices to check that there is a path between the corresponding two vertices in the graph. Given an undirected graph and two distinct vertices 𝑢 and 𝑣, check if there is a path between 𝑢 and 𝑣.
* Sample.
```
Input: 4 4
       1 2
       3 2
       4 3
       1 4
       1 4

```
* Output: 1

In this graph, there are two paths between vertices 1 and 4: 1-4 and 1-2 3-4.

## connected_components.py

This program, given an undirected graph with 𝑛 vertices and 𝑚 edges, computes the number of connected components in it.
* Sample.
```
Input: 4 2
       1 2
       3 2

```
* Output: 2

There are two connected components here: {1, 2, 3} and {4}.


## acyclicity.py

This program checks whether a given directed graph with 𝑛 vertices and 𝑚 edges contains a cycle.
* Sample.
```
Input: 4 4
       1 2
       4 1
       2 3
       3 1

```
```
Output: 1

```
This graph contains a cycle: 3 → 1 → 2 → 3.


## toposort.py

This program computes a topological ordering of a given directed acyclic graph (DAG) with 𝑛 vertices and 𝑚 edges.
* Sample.
```
Input: 4 3
       1 2
       4 1
       3 1
```
```
Output: 4 3 1 2

```

## strongly_connected.py

This program computes the number of strongly connected components of a given directed graph with 𝑛 vertices and 𝑚 edges.
* Sample.
```
Input: 4 4
       1 2
       4 1
       2 3
       3 1


```
* Output: 2

This graph has two strongly connected components: {1, 3, 2}, {4}.
