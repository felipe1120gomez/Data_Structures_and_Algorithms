# Dynamic Programming

These scripts use the sys module to read the input data.
Press ctrl z after entering the data to run the script.

## change_dp.py

Algorithm that apply dynamic programming for solving the Money Change Problem for denominations 1, 3, and 4.
Sample.
Input: 34
Output: 9
34 = 3 + 3 + 4 + 4 + 4 + 4 + 4 + 4 + 4.

## edit_distance.py

Algorithm that computes the edit distance between two strings.
Sample.
Input: editing
       distance
Output: 5
An alignment of total cost 5

## lcs2.py

Algorithm that compute the length of a longest common subsequence of two sequences.
Sample.
Input: 3
       2 7 5
       2
       2 5
Output: 2
A common subsequence of length 2 is (2, 5).
The 3 and the 2 are the length of each lists.

## lcs3.py

Algorithm that compute the length of a longest common subsequence of three sequences.
Sample.
Input: 5
       8 3 2 1 7
       7
       8 2 1 3 8 10 7
       6
       6 8 3 1 4 7
Output: 3
One common subsequence of length 3 in this case is (8, 3, 7). Another one is (8, 1, 7).
5, 7 and 6 are the length of each lists.

## placing_parentheses.py

Algorithm to find the maximum possible value of the given arithmetic expression among different orders of applying arithmetic operations.
Sample.
Input: 5-8+7*4-8+9
Output: 200
200 = (5 − ((8 + 7) × (4 − (8 + 9))))

## primitive_calculator.py

A primitive calculator that can perform the following three operations with the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥.
Find the minimum number of operations needed to obtain the number 𝑛 starting from the number 1.
Sample.
Input: 96234
Output: 14
        1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
