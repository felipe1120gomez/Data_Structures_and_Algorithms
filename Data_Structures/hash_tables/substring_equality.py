# python3

import random

class StringProcessor:
    """
    A class to represent a string processor.

    ...

    Attributes
    ----------
    string : str()
        String to be processed
    mod_1 : int

    mod_2 : int

    mult : int
        Randomly chosen multiplier between 1 and 10^9
    hash_1 : list()
        Hash table with the values for the string evaluated in mod_1
    hash_1 : list()
        Hash table with the values for the string evaluated in mod_2

    Methods
    -------
    precomp_hash(self, mod):
        Returns a hash table of the string evaluated in mod_1 or mod_2

    equal(self, s_a, s_b, len_s):
        It takes a starting index for the substring 'a' another for the substring 'b'
        and the length of both. Returns whether both are the same or not.

    """

    def __init__(self, string):
        """
        Constructs all the necessary attributes for the string processor:

        Parameters
        ----------
        string : str()
            String to be processed
        mod_1 : int

        mod_2 : int

        mult : int
            Randomly chosen multiplier between 1 and 10^9
        hash_1 : list()
            Hash table with the values for the string evaluated in mod_1
        hash_1 : list()
            Hash table with the values for the string evaluated in mod_2

        """

        self.string = string
        self.mod_1 = 1000000007
        self.mod_2 = 1000000009
        self.mult = random.randint(1, self.mod_1 - 7)
        self.hash_1 = list()
        self.hash_2 = list()

    def precomp_hash(self, mod):
        '''Returns a hash table of the string evaluated in mod_1 or mod_2'''

        hash_table = [None] * (len(self.string) + 1)
        hash_table[0] = 0
        for i in range(1, len(self.string) + 1):
            hash_table[i] = (self.mult * hash_table[i - 1] + ord(self.string[i - 1])) % mod

        return hash_table

    def equal(self, s_a, s_b, len_s):
        '''It takes a starting index for the substring 'a' another for the substring 'b'
        and the length of both. Returns whether both are the same or not.'''

        if not self.hash_1: # Do it only once for performance reasons
            self.hash_1 = self.precomp_hash(self.mod_1)
            self.hash_2 = self.precomp_hash(self.mod_2)

        # polyhash function for modulo m1
        # pow(mult^len_s) We include the mod_ in the calculation to make it faster.
        polyhash_a_m1 = (self.hash_1[s_a + len_s] - pow(self.mult, len_s, self.mod_1) * self.hash_1[s_a]) % self.mod_1
        polyhash_b_m1 = (self.hash_1[s_b + len_s] - pow(self.mult, len_s, self.mod_1) * self.hash_1[s_b]) % self.mod_1

        if polyhash_a_m1 != polyhash_b_m1:
            return False

        # polyhash function for modulo m2
        polyhash_a_m2 = (self.hash_2[s_a + len_s] - pow(self.mult, len_s, self.mod_2) * self.hash_2[s_a]) % self.mod_2
        polyhash_b_m2 = (self.hash_2[s_b + len_s] - pow(self.mult, len_s, self.mod_2) * self.hash_2[s_b]) % self.mod_2

        if polyhash_a_m2 != polyhash_b_m2:
            return False

        # The substrings will only be the same if their hash values are the same
        # evaluated in both modules, this due to the probability of a collision.
        return True

if __name__ == '__main__':
    the_string = input()
    querys = int(input())
    solver = StringProcessor(the_string)
    for _ in range(querys):
        sub_a, sub_b, len_sub = map(int, input().split())
        print("Yes" if solver.equal(sub_a, sub_b, len_sub) else "No")
