"""Given nodes numbered from 0, n-1 and a list of edges, determine if the edges
make up a tree.
"""
import collections
import random


def is_valid(n, edges):
    
    # build dictionary that maps starting nodes to ending nodes
    graph = collections.defaultdict(list)
    for (x, y) in edges:
        graph[x].append(y)
        graph[y].append(x)

    # set containing nodes that have been visited
    visited = set()

    # dfs - returns false if cycle otherwise true
    def dfs(node, parent):

        # already visited this node -> cycle
        if node in visited:
            return False

        # add node
        visited.add(node)

        # visit child nodes
        for child in graph[node]:

            # if child dfs found a cycle, then contains a cycle
            # skip trivial cycles
            if child != parent and not dfs(child, node):
                return False

        # no cycles found
        return True

    # test if contains cycles and if connected
    return dfs(0, -1) and len(visited) == n


if __name__ == "__main__":
    test_cases = [
        (5, [(0,1), (0,2), (0,3), (1,4)], True),
        (5, [(0,1), (1,2), (2,3), (1,3), (1,4)], False),
    ]
    for (n, edges, desired) in test_cases:
        assert is_valid(n, edges) == desired, f"n={n}, edges={edges}, desired={desired}"

