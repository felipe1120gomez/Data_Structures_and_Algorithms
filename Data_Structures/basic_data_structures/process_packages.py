# python3

from collections import namedtuple
from collections import deque

Request = namedtuple("Request", ["arrived", "process"])
Response = namedtuple("Response", ["dropped", "started"])


class Buffer:
    """
    A class to represent a buffer.

    ...

    Attributes
    ----------
    size : int
        size of the buffer
    finish_time : deque
        representation of the buffer as a deque

    Methods
    -------
    process(self, request):
        It processes the packets, determines if there is space in the buffer for it,
        which processor will take care of the packet and when it will start to process.
    """

    def __init__(self, size):
        """
        Constructs all the necessary attributes for the buffer object.

        Parameters
        ----------
            size : int
                size of the buffer
            finish_time : deque
                representation of the buffer as a deque
        """

        self.size = size
        self.finish_time = deque()

    def process(self, request):
        '''
        processing the packets has a network buffer of fixed size 𝑆.
        When packets arrive, they are stored in the buffer before being processed.
        However, if the buffer is full when a packet arrives
        (there are 𝑆 packets which have arrived before this packet,
        and the computer hasn’t finished processing any of them),
        it is dropped and won’t be processed at all.

        For each packet return either the moment of time (in milliseconds)
        when the processor began processing it or −1 if the packet was dropped

        '''

        # If there is space in the buffer
        if len(self.finish_time) < self.size:

            if len(self.finish_time) > 0: # If there are already packages
                prev_start = self.finish_time[-1][0]
                prev_pro = self.finish_time[-1][1]
                # Time it took to process the previous packet
                start_time = prev_start + prev_pro

                # If the package arrived before the previous one was processed
                if start_time > request.arrived:
                    self.finish_time.append([start_time, request.process])
                    return Response(False, start_time)

                # If the package arrived after the previous one was processed
                self.finish_time.append([request.arrived, request.process])
                return Response(False, request.arrived)

            elif len(self.finish_time) == 0: # If there are no packages
                self.finish_time.append([request.arrived, request.process])
                return Response(False, request.arrived)

        elif len(self.finish_time) == self.size: # If the buffer is full
            first_start = self.finish_time[0][0]
            first_pro = self.finish_time[0][1]

            # If the oldest package has already been processed
            if (first_start + first_pro) <= request.arrived:
                packet = self.finish_time.popleft() # Is removed from the buffer
                prev_start = packet[0]
                prev_pro = packet[1]

            if len(self.finish_time) < self.size:
                # If it was the only package its processing time is used
                if len(self.finish_time) == 0:
                    start_time = prev_start + prev_pro

                # If it was not the only one, the processing time of the last packet is used
                else:
                    prev_start = self.finish_time[-1][0]
                    prev_pro = self.finish_time[-1][1]
                    start_time = prev_start + prev_pro

                # If the package arrived before the previous one was processed
                if start_time > request.arrived:
                    self.finish_time.append([start_time, request.process])
                    return Response(False, start_time)

                # If the package arrived after the previous one was processed
                self.finish_time.append([request.arrived, request.process])
                return Response(False, request.arrived)

            # If there is no space in the buffer, the packet is dropped
            return Response(True, request.arrived)


def process_requests(requests, buffer):
    '''Send the packets one by one to the buffer to be processed.
    Returns a list with the information of the packages already processed.'''

    responses = list()
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())

    if n_requests == 0: # if there were no packages
        return

    requests = list()
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started if not response.dropped else -1)


if __name__ == "__main__":
    main()
