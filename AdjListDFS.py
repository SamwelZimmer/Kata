"""Not sure this actually functions properly"""

from typing import List, TypedDict


class GraphEdge(TypedDict):
    to: int
    weight: int


WeightedAdjacencyList = List[List[GraphEdge]]


def walk(graph: WeightedAdjacencyList, curr: int, needle: int, seen: List[bool], path: List[int]) -> bool:

    # base case: already seen the vertex (node) we don't need to look here again
    if seen[curr]:
        return False

    # update the seen array
    seen[curr] = True

    # # pre-recursion
    # add vertex to the path
    path.append(curr)

    # base case -> current node is what we're looking for
    if curr == needle:
        return True

    # # recurse
    # get the list of edges of the current vertex
    list = graph[curr]

    # loop through each of the edges (child vertices)
    for i in range(len(list)):
        edge = list[i]

        # if finding the needle when walking this path then finish searching
        if walk(graph, edge["to"], needle, seen, path):
            return True

    # # post-recursion
    #  remove the vertex
    path.pop()

    return False


def dfs(graph: WeightedAdjacencyList, source: int, needle: int) -> List[int] or None:

    # init arrays to store the seen and path vertices
    seen: List[bool] = [False] * len(graph)
    path: List[int] = []

    # search through the graph
    walk(graph, source, needle, seen, path)

    # return path if it exists, otherwise null
    if len(path) == 0:
        return None

    return path


def test_dfs():

    # Example graph:
    # 0 --1-- 1
    # |      /
    # |     /
    # 2    2
    # |   /
    # |  /
    # 3
    graph = [
        [{"to": 1, "weight": 1}, {"to": 3, "weight": 2}],
        [{"to": 2, "weight": 2}],
        [{"to": 3, "weight": 1}],
        []
    ]

    # Test 1: Path from 0 to 3
    assert dfs(graph, 0, 3) == [0, 3]

    # Test 2: Path from 0 to 2
    assert dfs(graph, 0, 2) == [0, 1, 2]

    # Test 3: Path from 1 to 3
    assert dfs(graph, 1, 3) == [1, 2, 3]

    # Test 4: Path from 2 to 0 (no such path)
    assert dfs(graph, 2, 0) is None

    # Test 5: Path from 0 to 0
    assert dfs(graph, 0, 0) == [0]

    print("All tests passed!")

test_dfs()


