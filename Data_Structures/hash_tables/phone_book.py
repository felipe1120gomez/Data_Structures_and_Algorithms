# python3

class Query:
    """
    A class to represent a user query.

    ...

    Attributes
    ----------
    type : str()
        Type of query: add, del or find
    number : int
        Phone number
    nane : str()
        Contact name

    Methods
    -------

    """

    def __init__(self, query):
        """
        Constructs all the necessary attributes for the user query:

        Parameters
        ----------
            type : str()
                Type of query: add, del or find
            number : int
                Phone number
            nane : str()
                Contact name
        """

        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    '''It reads the user input and passes it to the Query class.'''

    num_que = int(input())
    return [Query(input().split()) for i in range(num_que)]

def write_responses(result):
    '''Print the result returned by process_queries()'''

    print('\n'.join(result))

def process_queries(queries):
    '''
    Process the following types of user’s queries:

    ∙ add number name. It means that the user adds a person with name name and phone number
    number to the phone book. If there exists a user with such number already, then your manager
    has to overwrite the corresponding name.

    ∙ del number. It means that the manager should erase a person with number number from the phone
    book. If there is no such person, then it should just ignore the query.

    ∙ find number. It means that the user looks for a person with phone number number. The manager
    should reply with the appropriate name, or with string “not found" (without quotes) if there is
    no such person in the book.
    '''

    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    # [0...9999999] indexes with None to save memory.
    contacts = [None] * (10 ** 7) # 7 Since it is the maximum number of digits that a number will have.
    for cur_query in queries:
        # The index represents the number, key = index, value = None or name.
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            if contacts[cur_query.number] is not None:
                contacts[cur_query.number] = cur_query.name
            else: # otherwise, just add it
                contacts[cur_query.number] = cur_query.name

        elif cur_query.type == 'del': # Delete contact
            if contacts[cur_query.number] is not None:
                contacts[cur_query.number] = None

        else:
            response = 'not found' # Find contact
            if contacts[cur_query.number] is not None:
                response = contacts[cur_query.number]
            result.append(response)

    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

# Although a dictionary can be used to solve this problem with more efficient
# memory usage, the idea is to use ¨direct addressing scheme¨ for learning.
# memory usage = O(10^7), improved by using None as the initial value.
