#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # All tickets 
    cache = {}

    # Add all tickets to cache 
    for t in tickets: 
        cache[t.source] = t.destination 

    # List that returns destination 
    itinerary = []

    # Which stop we're currently on 
    current = 'NONE'

    for i in range(length):

        # Append the value to the trip list 
        itinerary.append(cache[current])

        # Set a new current 
        current = cache[current]

    return itinerary

    