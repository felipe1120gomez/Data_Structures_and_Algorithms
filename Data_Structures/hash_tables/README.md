# Hash Tables and Hash Functions

## phone_book.py

A program that implements a simple phone book manager. It should be able to process the
following types of user’s queries:

* add number name. It means that the user adds a person with a name and phone number to the phone book. If there exists a user with such a number already, then your manager has to overwrite the corresponding name.
* del number. It means that the manager should erase a person with a number from the phone book. If there is no such person, then it should just ignore the query.
* find the number. It means that the user looks for a person with a phone number number. The manager should reply with the appropriate name, or with the string “not found" (without quotes) if there is no such person in the book.

* Sample.
```
Input: 8
       find 3839442
       add 123456 me
       add 0 granny
       find 0
       find 123456
       del 0
       del 0
       find 0

```
```
Output: not found
        granny
        me
        not found

```

## hash_chains.py

This program supports the following kinds of queries:

* add string — insert the string into the table. If there is already such a string in the hash table, then just ignore the query.
* del string — remove the string from the table. If there is no such string in the hash table, then just ignore the query.
* find string — output “yes" or “no" (without quotes) depending on whether the table contains a string or not.
* check 𝑖 — output the content of the 𝑖-th list in the table. Use spaces to separate the elements of the list. If 𝑖-th list is empty, output a blank line.

* Sample.
```
Input: 4
       8
       add test
       add test
       find test
       del test
       find test
       find Test
       add Test
       find Test

```
```
Output: yes
        no
        no
        yes

```

Adding “test" twice is the same as adding “test" once, so first find returns “yes". After del, “test" is no longer in the hash table. The first-time find doesn’t find “Test” because it was not added before, and strings are case-sensitive in this problem. The second time “Test” can be found because it has just been added.

## hash_substring.py

A program that implements Rabin–Karp’s algorithm for searching the given pattern in the given text.

* Sample.
```
Input: Test
       testTesttesT

```
```
Output: 4

```
Pattern and text are case-sensitive in this problem. Pattern 𝑇 𝑒𝑠𝑡 can only be found in position 4 in the text 𝑡𝑒𝑠𝑡𝑇𝑒𝑠𝑡𝑡𝑒𝑠𝑇.


## substring_equality.py

This program is able to preprocess a given string 𝑠 to answer any query of the form “are these two substrings of 𝑠 equal?”

* Sample.
```
Input: trololo
       4
       0 0 7
       2 4 3
       3 5 1
       1 3 2
```
```
Output: Yes
        Yes
        Yes
        No

```
* 0 0 7 → trololo = trololo
* 2 4 3 → trololo = trololo
* 3 5 1 → trololo = trololo
* 1 3 2 → trololo ̸= trololo
