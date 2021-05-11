# python3

class Heap():
    """
    A class to represent a min-heap.

    ...

    Attributes
    ----------
    array : list()
        representation of the min-heap as a list
    swaps : list()
        list of swaps needed to get a min-heap

    Methods
    -------
    l_child(self, i):
        Returns the left child of the node.

    r_child(self, i):
        Returns the right child of the node.

    shiftdown(self, i, s_z):
        It moves the node down until the condition that it is less than or equal
        to its children and greater than or equal to its parent is met.

    build(self):
        Pass the nodes to the shiftdown function to convert the array into a min-heap.
        And return the swaps needed to get a min-heap.
    """

    def __init__(self, array):
        """
        Constructs all the necessary attributes for the min-heap:

        Parameters
        ----------
            array : list()
                representation of the min-heap as a list
            swaps : list()
                list of swaps needed to get a min-heap
        """

        self.array = array
        self.swaps = list()

    def l_child(self, i):
        '''Returns the left child of the node.'''

        return (2 * i) + 1

    def r_child(self, i):
        '''Returns the right child of the node.'''

        return (2 * i) + 2

    def shiftdown(self, i, s_z):
        '''It moves the node down until the condition that it is less than or equal
        to its children and greater than or equal to its parent is met.'''

        size = s_z
        left = self.l_child(i)
        while i < size and left <= size: # While we are not in the bottom
            max_index = i
            # The following conditionals will define which child is the smallest
            if left <= size and self.array[left] < self.array[max_index]:
                max_index = left
            right = self.r_child(i)
            if right <= size and self.array[right] < self.array[max_index]:
                max_index = right
            if i != max_index: # Swap the father for the smallest child
                self.swaps.append((i, max_index))
                self.array[i], self.array[max_index] = self.array[max_index], self.array[i]
                i = max_index # Now we evaluate the new children in the new position
                left = self.l_child(i)
            else: # If there is no small child, we return to the build function
                break

    def build(self):
        '''Pass the nodes to the shiftdown function to convert the array into a min-heap.
        And return the swaps needed to get a min-heap.'''

        size = len(self.array) - 1
        # We only walk the upper half of the tree
        for node in range(size // 2, 0, -1): # First from the middle to the root
            self.shiftdown(node, size)
        for node in range(0, size // 2): # Then from the root to the middle
            self.shiftdown(node, size)
        return self.swaps

def build_heap(data):
    '''Converts an array to a min-heap.'''

    heap = Heap(data)
    return heap.build()

def main():
    n_nodes = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n_nodes

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
