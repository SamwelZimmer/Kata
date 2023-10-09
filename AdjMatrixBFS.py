from typing import List

WeightedAdjacencyMatrix = List[List[int]]


def bfs(graph: WeightedAdjacencyMatrix, source: int, needle: int) -> List[int]:

    # if source and needle are the same.
    if source == needle:
        return [source]

    # init arrays to store the seen vertices (nodes) and the previous vertices
    seen = [False] * len(graph)
    prev = [-1] * len(graph)

    # can mark the starting vertex as seen
    seen[source] = True

    # initialise a queue
    queue: List[int] = [source]

    # loop until the queue is empty
    while len(queue):

        # get first item in the queue
        curr = queue.pop(0)

        # exit the loop if we have found the desired node
        if curr == needle:
            break

        # get the edges of the current vertex and loop through them
        adjs = graph[curr]
        for i in range(len(adjs)):

            # if no edge then continue
            if adjs[i] == 0:
                continue

            # ignore if we've already seen the vertex
            if seen[i]:
                continue

            # update the seen and previous arrays
            seen[i] = True
            prev[i] = curr

            # add to the queue
            queue.append(i)

    # # build the path backwards
    # start at the desired end position
    curr = needle

    # init an array which stores the path through the graph
    out: List[int] = []

    # iterate until finding a point with no parent
    while prev[curr] != -1:

        # add current vertex to the path
        out.append(curr)

        # set current vertex to its parent
        curr = prev[curr]

    # if there is a path through the graph
    if len(out):
        out.reverse()
        return [source] + out

    # otherwise return empty array
    return []


def test_bfs():
    # Simple test case
    graph1 = [
        [0, 1, 0, 0],
        [1, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0]
    ]
    assert bfs(graph1, 0, 3) == [0, 1, 3]

    # Test case where start and end nodes are the same
    assert bfs(graph1, 0, 0) == [0]

    # Test case where no path exists
    graph2 = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ]
    assert bfs(graph2, 0, 3) == []

    # Larger test case
    graph3 = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]
    assert bfs(graph3, 0, 4) == [0, 2, 3, 4]

    print("All tests passed!")


test_bfs()
