# Binary Search Trees

## tree_orders.py

This program implements in-order, pre-order, and post-order traversals of a binary tree.

* Sample.
```
Input: 5
       4 1 2
       2 3 4
       5 -1 -1
       1 -1 -1
       3 -1 -1


```
```
Output: 1 2 3 4 5
        4 2 1 3 5
        1 3 2 5 4


```

## is_bst.py

This program, given a binary tree with integers as its keys, test whether it is a correct binary search tree. The definition of the binary search tree is the following: for any node of the tree, if its key is π₯, then for any node in its left subtree its key must be strictly less than π₯, and for any node in its right subtree its key must be strictly greater than π₯. In other words, smaller elements are to the left, and bigger elements are to the right.

* Sample.
```
Input: 4
       4 1 -1
       2 2 3
       1 -1 -1
       5 -1 -1


```
```
Output: INCORRECT

```
Node 5 is in the left subtree of the root, but it is bigger than the key 4 in the root.

## is_bst_hard.py

This program, given a binary tree with integers as its keys, test whether it is a correct binary search tree. Note that there can be duplicate integers in the tree, and this is allowed. The definition of the binary search tree in such case is the following: for any node of the tree, if its key is π₯, then for any node in its left subtree its key must be strictly less than π₯, and for any node in its right subtree its key must be greater than or equal to π₯. In other words, smaller elements are to the left, bigger elements are to the right, and duplicates are always to the right.

* Sample.
```
Input: 3
       2 1 2
       1 -1 -1
       2 -1 -1

```
```
Output: CORRECT

```
Duplicate keys are allowed, and they should always be in the right subtree of the first duplicated element.


## set_range_sum.py

This program implements a data structure that stores a set π of integers with the following allowed operations:

* add(π) β add integer π into the set π (if it was there already, the set doesnβt change).
* del(π) β remove integer π from the set π (if there was no such element, nothing happens).
* find(π) β check whether π is in the set π or not.
* sum(π, π) β output the sum of all elements π£ in π such that π β€ π£ β€ π.

However, to make sure that the solution can work in an online fashion, each request will actually depend on the result of the last sum request. Denote π = 1 000 000 001. At any moment, let π₯ be the result of the last sum operation, or just 0 if there were no sum operations before. Then

* β+ i" means add((π + π₯) mod π),
* β- i" means del((π + π₯) mod π),
* β? i" means find((π + π₯) mod π),
* βs l r" means sum((π + π₯) mod π,(π + π₯) mod π).

* Sample.
```
Input: 15
       ? 1
       + 1
       ? 1
       + 2
       s 1 2
       + 1000000000
       ? 1000000000
       - 1000000000
       ? 1000000000
       s 999999999 1000000000
       - 2
       ? 2
       - 0
       + 9
       s 0 9
```
```
Output: Not found
        Found
        3
        Found
        Not found
        1
        Not found
        10

```
For the first 5 queries, π₯ = 0. For the next 5 queries, π₯ = 3. For the next 5 queries, π₯ = 1. The actual list of operations is:

* find(1)
* add(1)
* find(1)
* add(2)
* sum(1, 2) β 3
* add(2)
* find(2) β Found
* del(2)
* find(2) β Not found
* sum(1, 2) β 1
* del(3)
* find(3) β Not found
* del(1)
* add(10)
* sum(1, 10) β 10

Adding the same element twice doesnβt change the set. Attempts to remove an element that is not in the set are ignored.
