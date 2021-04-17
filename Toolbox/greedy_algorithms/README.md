## Greedy Algorithms

Some of these scripts use the sys module to read the input data.
Press ctrl z after entering the data to run the script.

## car_fueling.py

Compute the minimum number of refills needed to complete a trip.
* Sample.
```
Input: 950
       400
       4
       200 375 550 750
```
* Output: 2

The distance between the cities is 950, the car can travel at most 400 miles on a full tank. It suffices to make two refills: at points 375 and 750. This is the minimum number of refills as with a single refill one would only be able to travel at most 800 miles.

## change_coin.py

Algorithm to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.
* Sample.
* Input: 28
* Output: 6

28 = 10 + 10 + 5 + 1 + 1 + 1.

## covering_segments.py

Return the minimum number 𝑚 of points on the first line and the integer coordinates of 𝑚 points (separated by spaces) on the second line.
* Sample.
```
Input: 4
       4 7
       1 3
       2 5
       5 6
Output: 2
        3 6
```

The second and the third segments contain the point with coordinate 3 while the first and the fourth segments contain the point with coordinate 6. All the four segments cannot be covered by a single point, since the segments [1, 3] and [5, 6] are disjoint.

## different_summands.py

Algorithm to represent a given positive integer 𝑛 as a sum of as many pairwise distinct positive integers as possible.
* Sample.
* Input: 8
```
Output: 3
        1 2 5
```

## dot_product.py

Look at the Docstring of the function.
* Sample.
```
Input: 3
       1 3 -5
       -2 4 1
```
* Output: 23

23 = 3 · 4 + 1 · 1 + (−5) · (−2).

## fractional_knapsack.py

Return the maximal value of fractions of items that fit into the knapsack.
* Sample.
```
Input: 3 50
       60 20
       100 50
       120 30
```
* Output: 180.0000

To achieve the value 180, we take the first item and the third item into the bag.

## largest_number.py

Algorithm to compose the largest number out of a set of integers.
* Sample.
```
Input: 2
       21 2
```
* Output: 221
