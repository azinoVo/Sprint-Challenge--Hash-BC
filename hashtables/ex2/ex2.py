#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

# We can hash each ticket such that the starting location is the key
# and the destination is the value. Then, when constructing the entire
# route, the `i`th location in the route can be found by checking the
# hash table for the `i-1`th location.


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # starting place
    for ticket in tickets:
        hash_table_insert(
            hashtable, ticket.source, ticket.destination)
        if ticket.source is None:
            route[0] = ticket.destination
        elif ticket.destination is None:
            route[-1] = ticket.source
    print("hashtable", route)
    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]
result = reconstruct_trip(tickets, 3)
print("Result", result)
