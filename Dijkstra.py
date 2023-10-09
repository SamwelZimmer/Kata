"""
implementation of dijkstra's shortest path in a graph which is represented by an Adjacency List

this algo has not been tested
"""

from typing import List, TypedDict


class GraphEdge(TypedDict):
    to: int
    weight: int


WeightedAdjacencyList = List[List[GraphEdge]]


def hasUnvisited(seen: List[bool], dists: List[int]) -> bool:

    # visit each seen vertex and determine if it is false and distance is less than Infinity
    return any(not s and dists[i] < float('inf') for i, s in enumerate(seen))


def getLowestUnvisited(seen: List[bool], dists: List[int]) -> int:
    idx = -1
    lowest_distance = float('inf')

    for i in range(len(seen)):

        # if already seen then move on
        if seen[i]:
            continue

        # if the current distance is smaller than the lowest recorded distance
        if lowest_distance > dists[i]:
            lowest_distance = dists[i]
            idx = i

    # return index of the lowest distance
    return idx


def dijkstra_list(source: int, sink: int, arr: WeightedAdjacencyList) -> List[int]:

    # init an array to store the nodes which have been seen and "parent" nodes
    seen: List[bool] = [False] * len(arr)
    prev: List[int] = [-1] * len(arr)

    # init an array to store node distances (if unseen set it to an infinitely large number)
    dists: List[int] = [float('inf')] * len(arr)

    # source node is already at the source
    dists[source] = 0

    while hasUnvisited(seen, dists):

        # get the current vertex
        curr = getLowestUnvisited(seen, dists)

        # update seen array
        seen[curr] = True

        # list of edge for the current vertex
        adjs = arr[curr]

        # loop through each edge
        for i in range(len(adjs)):
            edge = adjs[i]

            # if this node already seen then continue
            if seen[edge["to"]]:
                continue

            # distance from the node
            dist = dists[curr] + edge["weight"]

            # if this distance is less than the known distance to this edge
            if dist < dists[edge["to"]]:

                # update to the new, smaller distance
                dists[edge["to"]] = dist
                prev[edge["to"]] = curr

    # list to store the path
    out: List[int] = []

    # init the current node to our target node
    curr = sink

    # iterate until the node has not "parents"
    while prev[curr] != -1:

        # add to the path
        out.append(curr)

        # update the current to the parent
        curr = prev[curr]

    # return the path
    out.append(source)
    out.reverse()
    return out
