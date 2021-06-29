# Coping with NP-completeness

## circuit_design.py

This script reduces a Very Large-Scale Integration problem to a 2-SAT problem — a special case of the SAT problem in which each clause contains exactly 2 variables. If the 2-CNF formula in the input is unsatisfiable, output just the word UNSATISFIABLE. If the 2-CNF formula in the input is satisfiable, output the word SATISFIABLE on the first line and the corresponding assignment of variables on the second line. For each 𝑥𝑖 in order from 𝑥1 to 𝑥𝑉, output 𝑖 if 𝑥𝑖 = 1 or −𝑖 if 𝑥𝑖 = 0. For example, if a formula is satisfied by assignment 𝑥1 = 0, 𝑥2 = 1, 𝑥3 = 0, output “-1 2 -3” on the second line.
* Sample.
```
Input: 3 3
       1 -3
       -1 2
       -2 -3

```
```
Output: SATISFIABLE
        1 2 -3

```

The input formula is (𝑥1 𝑂𝑅 𝑥3) 𝐴𝑁𝐷 (𝑥1 𝑂𝑅 𝑥2) 𝐴𝑁𝐷 (𝑥2 𝑂𝑅 𝑥3), and the assignment 𝑥1 = 1, 𝑥2 = 1, 𝑥3 = 0 satisfies it.


## plan_party.py

You’re planning a company party. You’d like to invite the coolest people, and you’ve assigned each
one of them a fun factor — the more the fun factor, the cooler is the person. You want to maximize the
total fun factor (sum of the fun factors of all the invited people). However, you can’t invite everyone,
because if the direct boss of some invited person is also invited, it will be awkward. Find out what is
the maximum possible total fun factor.

This program finds the maximum possible total fun factor of the party (the sum of fun factors of all the invited people).
* Sample.
```
Input: 5
       1 5 3 7 5
       5 4
       2 3
       4 2
       1 2


```
* Output: 11

We can invite 1, 3, and 4 for a total fun factor of 11. If we invite 2, we cannot invite 1, 3, or 4, so the total fun factor will be at most 10, thus we don’t invite 2 in the optimal solution. If we don’t invite 4 also, we will get a fun factor of at most 1 + 3 + 5 = 9, so we must invite 4. But then we can’t invite 5, so we invite also 1 and 3 and get the total fun factor of 11.
