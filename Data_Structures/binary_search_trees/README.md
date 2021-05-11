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

This program, given a binary tree with integers as its keys, test whether it is a correct binary search tree. The definition of the binary search tree is the following: for any node of the tree, if its key is 𝑥, then for any node in its left subtree its key must be strictly less than 𝑥, and for any node in its right subtree its key must be strictly greater than 𝑥. In other words, smaller elements are to the left, and bigger elements are to the right.

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

This program, given a binary tree with integers as its keys, test whether it is a correct binary search tree. Note that there can be duplicate integers in the tree, and this is allowed. The definition of the binary search tree in such case is the following: for any node of the tree, if its key is 𝑥, then for any node in its left subtree its key must be strictly less than 𝑥, and for any node in its right subtree its key must be greater than or equal to 𝑥. In other words, smaller elements are to the left, bigger elements are to the right, and duplicates are always to the right.

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

This program implements a data structure that stores a set 𝑆 of integers with the following allowed operations:

* add(𝑖) — add integer 𝑖 into the set 𝑆 (if it was there already, the set doesn’t change).
* del(𝑖) — remove integer 𝑖 from the set 𝑆 (if there was no such element, nothing happens).
* find(𝑖) — check whether 𝑖 is in the set 𝑆 or not.
* sum(𝑙, 𝑟) — output the sum of all elements 𝑣 in 𝑆 such that 𝑙 ≤ 𝑣 ≤ 𝑟.

However, to make sure that the solution can work in an online fashion, each request will actually depend on the result of the last sum request. Denote 𝑀 = 1 000 000 001. At any moment, let 𝑥 be the result of the last sum operation, or just 0 if there were no sum operations before. Then

* “+ i" means add((𝑖 + 𝑥) mod 𝑀),
* “- i" means del((𝑖 + 𝑥) mod 𝑀),
* “? i" means find((𝑖 + 𝑥) mod 𝑀),
* “s l r" means sum((𝑙 + 𝑥) mod 𝑀,(𝑟 + 𝑥) mod 𝑀).

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
For the first 5 queries, 𝑥 = 0. For the next 5 queries, 𝑥 = 3. For the next 5 queries, 𝑥 = 1. The actual list of operations is:

* find(1)
* add(1)
* find(1)
* add(2)
* sum(1, 2) → 3
* add(2)
* find(2) → Found
* del(2)
* find(2) → Not found
* sum(1, 2) → 1
* del(3)
* find(3) → Not found
* del(1)
* add(10)
* sum(1, 10) → 10

Adding the same element twice doesn’t change the set. Attempts to remove an element that is not in the set are ignored.
