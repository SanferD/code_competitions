"""Reconstruct itinerary given a list of tickets
"""
import collections
import copy


class InvalidCombination(Exception):
    pass


def reconstruct(tickets):
    
    # sort tickets in lexical order
    tickets.sort()

    # build a dictionary that maps source to list of destinations
    destinations = collections.defaultdict(list)
    for (src, dst) in tickets:
        destinations[src].append(dst)

    #~
    # hop around in lexical order of travel, starting at jfk, and build itinerary

    # helper function that will build the itinerary
    # by traversing the graph until it finds a valid sequence
    def hop(src, itinerary, destinations):

        # base case: visited all destinations
        if len(itinerary) == len(tickets) + 1:
            return itinerary

        # try the next hop spot
        for (i, dst) in enumerate(destinations[src]):

            # remove given dst from destinations so future calls don't reuse it
            destinations[src].pop(i)

            # add dst
            itinerary.append(dst)

            # attempt to build the itineray with the choice

            try:
                #success
                return hop(dst, itinerary, destinations)
            except InvalidCombination:
                #fail - backtrack
                destinations[src].insert(i, dst)
                itinerary.pop()

        # couldn't find a valid combination - raise
        raise InvalidCombination()

    # initial call + return the built itinerary
    return hop("JFK", ["JFK"], destinations)


if __name__ == "__main__":
    test_cases = [
        ([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]], ["JFK","MUC","LHR","SFO","SJC"]),
        ([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]], ["JFK","ATL","JFK","SFO","ATL","SFO"]),
        ([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]],["JFK","NRT","JFK","KUL"]),
    ]

    for (tickets, desired) in test_cases:
        found = reconstruct(tickets)
        assert found == desired, f"tickets={tickets}, found={found}, desried={desired}"

