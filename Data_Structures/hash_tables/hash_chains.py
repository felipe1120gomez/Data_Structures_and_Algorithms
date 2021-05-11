# python3

class Query:
    """
    A class to represent a user query.

    ...

    Attributes
    ----------
    type : str()
        Type of query: add, del, find or check
    ind : int
        Index where the chain will be saved
    string : str()
        String

    Methods
    -------

    """

    def __init__(self, query):
        """
        Constructs all the necessary attributes for the user query:

        Parameters
        ----------
        type : str()
            Type of query: add, del, find or check
        ind : int
            Index where the chain will be saved
        string : str()
            String
        """

        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.string = query[1]


class QueryProcessor:
    """
    A class to represent a query processor.

    ...

    Attributes
    ----------
    bucket_count : int
        Number of queries
    elems : list()
        Hash table using the chaining scheme
    _multiplier : int

    _prime : int

    Methods
    -------
    read_query(self):
        Recive the queries and passes it to the Query class

    write_search_result(self, was_found):
        Returns if a word was found in a chain

    write_chain(self, chain):
        Returns the content of the chain

    _hash_func(self, string):
        Returns the index(chain) where the string will be stored

    process_query(self, query):
        Process the following types of user’s queries:
        add, del, find or check

    process_queries(self):
        Call the function process_query()

    """

    def __init__(self, bucket_count):
        """
        Constructs all the necessary attributes for the query processor:

        Parameters
        ----------
        bucket_count : int
            Number of queries
        elems : list()
            Hash table using the chaining scheme
        _multiplier : int

        _prime : int

        """

        self.bucket_count = bucket_count
        # store all chains(lists) in one list
        # Table with cardinality m = bucket_count
        self.elems = [None] * self.bucket_count
        self._multiplier = 263
        self._prime = 1000000007

    def read_query(self):
        '''Recive the queries and passes it to the Query class.'''

        return Query(input().split())

    def write_search_result(self, was_found):
        '''Returns if a word was found in a chain'''

        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        '''Returns the content of the chain'''

        if chain:
            print(' '.join(chain))
        else:
            print(' ')

    def _hash_func(self, string):
        '''Returns the index(chain) where the string will be stored'''

        ans = 0
        for char in reversed(string):
            ans = (ans * self._multiplier + ord(char)) % self._prime
        return ans % self.bucket_count

    def process_query(self, query):
        '''
        Process the following types of user’s queries:

        ∙ add string — insert string into the table.
        If there is already such string in the hash table, then just ignore the query.

        ∙ del string — remove string from the table.
        If there is no such string in the hash table, then just ignore the query.

        ∙ find string — output “yes" or “no" (without quotes)
        depending on whether the table contains string or not.

        ∙ check 𝑖 — output the content of the 𝑖-th list in the table.
        Use spaces to separate the elements of the list. If 𝑖-th list is empty, output a blank line.

        When inserting a new string into a hash chain,
        you must insert it in the beginning of the chain.
        '''

        if query.type == "check":
            if self.elems[query.ind] is not None:
                self.write_chain(self.elems[query.ind]) # The chain is passed to be printed
            else:
                self.write_chain([])

        else:
            ind_hash = self._hash_func(query.string)
            if self.elems[ind_hash] is not None:
                already_hash = True
            else:
                already_hash = False

            if query.type == 'find':
                if already_hash:
                    # Is passed to the function write_search_result() to see if it is in the chain
                    self.write_search_result(query.string in self.elems[ind_hash])
                else:
                    self.write_search_result(False)

            elif query.type == 'add':
                if not already_hash:
                    # The string is added, nested in a list(chain)
                    self.elems[ind_hash] = [query.string]
                else:
                    if query.string not in self.elems[ind_hash]:
                        # It is added at index 0 in the chain
                        self.elems[ind_hash].insert(0, query.string)
            else:
                if already_hash:
                    if query.string in self.elems[ind_hash]:
                        self.elems[ind_hash].remove(query.string)
                        if not self.elems[ind_hash]:
                            # Don't leave the chain empty
                            self.elems[ind_hash] = None

    def process_queries(self):
        '''Call the function process_query'''

        num_que = int(input())
        for _ in range(num_que):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket = int(input())
    proc = QueryProcessor(bucket)
    proc.process_queries()
