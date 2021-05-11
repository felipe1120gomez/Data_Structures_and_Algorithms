# python3

import random

def read_input():
    '''Reads the input'''

    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    '''Print the list of indexes'''

    print(' '.join(map(str, output)))

def poly_hash(last_sub, prime, ran_x):
    '''Returns the hash for the pattern and for each pattern size sub-strings.'''

    ans = 0
    for char in reversed(last_sub):
        ans = (ans * ran_x + ord(char)) % prime
    return ans

def pre_comp(text, pat_len, prime, ran_x):
    '''Returns a hash table with all the values for all
    pattern size sub-strings present in the text.'''

    size_array = (len(text) - pat_len) + 1
    size_pat = (len(text) - pat_len) - 1
    start = len(text) - pat_len

    array = [None] * size_array # Hash table

    last_sub = text[start:] # Last possible substring in the text (pattern)

    array[start] = poly_hash(last_sub, prime, ran_x) # Hash value for the last index

    the_y = 1
    for _ in range(1, pat_len + 1):
        the_y = (the_y * ran_x) % prime

    # Fill the table from back to front, with the hash values for each substring
    for j in range(size_pat, -1, -1):
        array[j] = (ran_x * array[j + 1] + ord(text[j]) - the_y * ord(text[j + pat_len])) % prime

    return array

def rabin_karp(pattern, text):
    '''Rabin–Karp’s function for searching the given pattern in the given text.
    Returns a list of indexes where the pattern starts.'''

    prime = 1000000007
    ran_x = random.randint(1, prime - 1)
    l_pattern = len(pattern)
    size = len(text) - l_pattern

    result = [] # List of indexes where the pattern starts

    p_hash = poly_hash(pattern, prime, ran_x) # Hash value of the pattern

    array = pre_comp(text, l_pattern, prime, ran_x)  # Hash table

    # Check if the index that contains the value of the substring matches the pattern
    for i in range(size + 1):
        end = i + l_pattern
        if p_hash != array[i]:
            continue
        elif text[i:end] == pattern:
            result.append(i) # Add the index where the substring starts to the result

    return result

if __name__ == '__main__':
    print_occurrences(rabin_karp(*read_input()))
