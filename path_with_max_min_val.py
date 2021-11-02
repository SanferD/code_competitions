"""Path with maximum minimum value
"""
import queue


def max_min_path(grid):

    # R and C
    R = len(grid)
    C = len(grid[0])
    
    # matrix which determines if the given index can be visited
    _row = [False]*C
    visited = [_row[:] for _ in range(R)]
    visited[0][0] = True

    #~
    # the idea is to traverse paths in a BFS manner, where larger path
    # nodes are traversed first.

    # priority queue to hold values - max grid values have higher priority
    candidates = queue.PriorityQueue()
    candidates.put(  (-grid[0][0], 0, 0)  )

    # initialize the max value
    max_min_val = float("inf")

    # traverse the matrix until the end is reached, updating the max value
    while not candidates.empty():

        # get the next candidate
        (val, i, j) = candidates.get()

        # update min value
        max_min_val = min(grid[i][j], max_min_val)

        # if this is the end, break
        if i == R-1 and j == C-1:
            break

        # otherwise traverse children if they're traversable
        for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

            # if not oob and not visited, then add the new candidate
            (i2, j2) = (i+di, j+dj)
            if 0 <= i2 < R and 0 <= j2 < C and not visited[i2][j2]:
                visited[i2][j2] = True
                candidates.put(  (-grid[i2][j2], i2, j2)  )

    # get the max min val
    return max_min_val


if __name__ == "__main__":
    test_cases = [
        ([[5,4,5],[1,2,6],[7,4,6]], 4),
        ([[2,2,1,2,2,2],[1,2,2,2,1,2]], 2),
        ([[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]], 3),
        ([[0,1,0,0,0,1],[0,1,1,0,0,0],[0,0,1,1,0,1],[0,1,1,1,1,0],[1,1,1,1,1,1]], 0),
    ]

    for (grid, desired) in test_cases:
        found = max_min_path(grid)
        assert desired == found, f"found={found}, desired={desired}, grid={grid}"
