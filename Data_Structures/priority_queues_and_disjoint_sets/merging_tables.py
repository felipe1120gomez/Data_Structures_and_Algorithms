# python3

class Database:
    """
    A class to represent a database.

    ...

    Attributes
    ----------
    row_counts : list()
        Number of rows in all tables
    max_row_count : int
        Maximum number of rows
    ranks : dict()
        Rank of each table, in the parent table it is equal to the height of the tree.
    rows : dict()
        Rows on each table.
    parents : dic()
        Parent of each table

    Methods
    -------
    merge(self, dst, src):
        Merge two tables with union by rank heuristic and path comprehension.

    get_parent(self, table):
        Returns the true parent of the table.
    """

    def __init__(self, row_counts):
        """
        Constructs all the necessary attributes for the min-heap:

        Parameters
        ----------
            row_counts : list()
                Number of rows in all tables
            max_row_count : int
                Maximum number of rows
            ranks : dict()
                Rank of each table, in the parent table it is equal to the height of the tree.
            rows : dict()
                Rows on each table.
            parents : dic()
                Parent of each table
        """

        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        # Dictionaries to find tables in O(1).
        self.ranks = {i: 1 for i in range(len(self.row_counts))} # Tables and ranks
        self.rows = {i: self.row_counts[i] for i in range(len(self.row_counts))} # Tables and rows
        self.parents = {i: i for i in range(n_tables)} # Tables and parents

    def merge(self, dst, src):
        '''Merge two tables with union by rank heuristic and path comprehension.'''

        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False # Already merged

        # Merge the smallest tree to the largest
        if self.ranks[dst_parent] >= self.ranks[src_parent]:

            self.rows[dst_parent] += self.rows[src_parent] # Copy rows from one table to another
            self.rows[src_parent] = 0 # Remove rows from source table
            self.ranks[dst_parent] += self.ranks[src_parent] # Increase the rank of the destination table
            self.ranks[src_parent] = 0 # Rank of the source table at 0
            self.parents[src_parent] = dst_parent # compress path
            if self.rows[dst_parent] > self.max_row_count:
                self.max_row_count = self.rows[dst_parent] # update max_row

        else:
            self.rows[src_parent] += self.rows[dst_parent] # Copy rows from one table to another
            self.rows[dst_parent] = 0 # Remove rows from destination table
            self.ranks[src_parent] += self.ranks[dst_parent] # Increase the rank of the source table
            self.ranks[dst_parent] = 0 # Rank of the destination table at 0
            self.parents[dst_parent] = src_parent # compress path
            if self.rows[src_parent] > self.max_row_count:
                self.max_row_count = self.rows[src_parent] # update max_row

        return True

    def get_parent(self, table):
        '''Returns the true parent of the table.'''

        parent = self.parents.get(table)
        # keep going until find the true father
        while table != parent:
            table = parent
            parent = self.parents.get(table)
        return parent # true parent


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    d_b = Database(counts)
    for _ in range(n_queries):
        dst, src = map(int, input().split())
        d_b.merge(dst - 1, src - 1)
        print(d_b.max_row_count)


if __name__ == "__main__":
    main()
