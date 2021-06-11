# Algorithmic Challenges

## kmp.py

This program finds all occurrences of a pattern in a string, recall that different occurrences of a pattern can overlap with each other. For example, ATA occurs three times in CGATATATCCATAG.

* Sample.
```
Input: ATAT
       GATATATGCATATACTT

```
```
Output: 1 3 9

```
The pattern appears at positions 1, 3, and 9 in the text.

## suffix_array_long.py

This program constructs the suffix array of a string, but this time for a longer string.

* Sample.
```
Input: GAGAGAGA$

```
```
Output: 8 7 5 3 1 6 4 2 0

```
Sorted suffixes:
* 8 $
* 7 A$
* 5 AGA$
* 3 AGAGA$
* 1 AGAGAGA$
* 6 GA$
* 4 GAGA$
* 2 GAGAGA$
* 0 GAGAGAGA$

## suffix_array_matching.py

This program find all occurrences of a given collection of patterns in a string using the suffix array to solve the Multiple Pattern Matching Problem.

* Sample.
```
Input: ATATATA
       3
       ATA C TATAT

```
```
Output: 4 2 0 1

```
The pattern ATA appears at positions 0, 2, and 4, the pattern TATAT appears at position 1.
