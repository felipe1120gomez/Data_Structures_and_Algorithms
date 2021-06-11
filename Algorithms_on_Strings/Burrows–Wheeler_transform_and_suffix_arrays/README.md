# Burrows–Wheeler Transform and Suffix Arrays

## bwt.py

This program constructs the Burrows–Wheeler transform of a string.

* Sample.
```
Input: AGACATA$

```
```
Output: ATG$CAAA

```

## bwtinverse.py

This program reconstructs a string from its Burrows–Wheeler transform.

* Sample.
```
Input: AGGGAA$

```
```
Output: GAGAGA$

```

## bwmatching.py

This program returns a list of integers, where the 𝑖-th integer corresponds to the number of substring matches of the 𝑖-th member of Patterns in Text.

* Sample.
```
Input: AT$TCTATG
       2
       TCT TATG

```
```
Output: 0 0

```
Text = ATCGTTTA does not contain any occurrences of two given patterns.

## suffix_array.py

This program constructs the suffix array of a string.

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
