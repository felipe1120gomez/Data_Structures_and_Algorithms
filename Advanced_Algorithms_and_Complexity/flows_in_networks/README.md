# Flows in Networks

## evacuation.py

This script applies an algorithm for finding a maximum flow in a network to determine how fast people can be evacuated from the given city.
* Sample.
```
Input: 5 7
       1 2 2
       2 5 5
       1 3 6
       3 4 2
       4 5 1
       3 2 3
       2 4 1

```
* Output: 6

We can evacuate 2 people through route 1−2−5, additional 3 people through route 1−3−2−5, and 1 more person through route 1−3−4−5 — for a total of 6 people. It is impossible to evacuate more people each hour, as the total capacity of all roads incoming to the capital city 5 is 6 people per hour.


## airline_crews.py

This program applies an algorithm for finding maximum matching in a bipartite graph to assign airline crews to flights in the most efficient way.
* Sample.
```
Input: 3 4
       1 1 0 1
       0 1 0 0
       0 0 0 0


```
* Output: 1 2 -1

We can assign the first crew to the first flight and the second crew to the second flight, and no crews can work on the third flight, so this is an optimal assignment.


## stock_charts.py

This program determines the minimum number of overlaid charts to visualize all the stock price data you have.
* Sample.
```
Input: 3 3
       5 5 5
       4 4 6
       4 5 4

```
```
Output: 3

```
Each stock can be put on its own overlaid stock chart, of course. But no two stocks can be put on the same overlaid stock chart: first and second would intersect between points 2 and 3, first and third would touch in point 2, second and third would touch in point 1.
