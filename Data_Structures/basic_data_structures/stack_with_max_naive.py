#python3

class StackWithMax():
    """
    A class to represent a stack with max.

    ...

    Attributes
    ----------
    __stack : list()
        representation of the stack as a list
    __max : list()
        list of maximum values in stack

    Methods
    -------
    push_stack(self, num):
        Add the number to the stack, also from the list of maximums if
        it is greater than or equal to the last maximum value in the list.

    pop_stack(self):
        Remove the last element added to the stack,
        also from the list of maximums if it is equal to the last maximum value in the list.

    max_stack(self):
        Returns the maximum value on the stack.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the stack with max:

        Parameters
        ----------
            __stack : list()
                representation of the stack as a list
            __max : list()
                list of maximum values in stack
        """

        self.__stack = list()
        self.__max = list() # Stores maximum values. [a <= b <= . . . y <= z]

    def push_stack(self, num):
        '''Add the number to the stack, also from the list of maximums if
        it is greater than or equal to the last maximum value in the list.'''

        self.__stack.append(num)
        if not self.__max: # If it is empty, it is added without problem.
            self.__max.append(num)
        # A new maximum is only added if it is >= to the last maximum
        elif self.__max and num >= self.__max[-1]:
            self.__max.append(num)

    def pop_stack(self):
        '''Remove the last element added to the stack,
        also from the list of maximums if it is equal to the last maximum value in the list.'''

        assert len(self.__stack)
        num = self.__stack.pop()
        # If the eliminated number is equal to the maximum, we also eliminate the maximum
        if num == self.__max[-1]:
            self.__max.pop()

    def max_stack(self):
        '''Returns the maximum value on the stack.'''

        assert len(self.__max)
        return self.__max[-1] # The maximum is the last element.


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(input())
    for _ in range(num_queries):
        query = input().split()

        if query[0] == "push":
            stack.push_stack(int(query[1]))
        elif query[0] == "pop":
            stack.pop_stack()
        elif query[0] == "max":
            print(stack.max_stack())
        else:
            assert 0
