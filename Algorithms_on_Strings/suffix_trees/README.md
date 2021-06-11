# Suffix Trees

## trie.py

This program constructs a trie from a collection of patterns.
* The trie has a single root node with indegree 0, denoted root.
* Each edge of Trie(Patterns) is labeled with a letter of the alphabet.
* Edges leading out of a given node have distinct labels.
* Every string in Patterns is spelled out by concatenating the letters along some path from the root downward.
* Every path from the root to a leaf, or node with outdegree 0, spells a string from Patterns.

* Sample.
```
Input: 3
       AT
       AG
       AC

```
```
Output: 0->1:A
        1->4:C
        1->3:G
        1->2:T

```

## trie_matching.py

This program finds all starting positions in Text where a string from Patterns appears as a substring in increasing order.

* Sample.
```
Input: AATCGGGTTCAATCGGGGT
       2
       ATCG
       GGGT

```
```
Output: 1 4 11 15

```
The pattern ATCG appears at positions 1 and 11, the pattern GGGT appears at positions 4 and 15.

## trie_matching_extended.py

This program finds all starting positions in Text where a string from Patterns appears as a substring in increasing order, this algorithm can handle correctly cases when one of the patterns is a prefix of another one.
* Sample.
```
Input: ACATA
       3
       AT
       A
       AG

```
```
Output: 0 2 4

```
Text contains occurrences of A at positions 0, 2, and 4, as well as an occurrence of AT at position 2.

## suffix_tree.py

This program constructs the suffix tree of a string.
* Sample.
```
Input: ACA$

```
```
Output: $
        A
        $
        CA$
        CA$
```

## non_shared_substring.py

This program finds the shortest substring of one string that does not appear in another string.
* Sample.
```
Input: CCAAGCTGCTAGAGG
       CATGCTGGGCTGGCT
```
```
Output: AA

```
In this case, Text2 contains all symbols A, C, G, T, that is, all substrings of Text1 of length 1. At the same time, Text2 does not contain AA, hence it is a shortest substring of Text1 that does not appear in Text2.
