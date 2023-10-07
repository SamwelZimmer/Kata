"""
Implementation of Depth First Search (DFS) on a Binary Search Tree (BST).

Not including insertion or deletion
"""


class BinaryNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def search(curr: BinaryNode, needle: int) -> bool:

    # base case 1: node is null
    if not curr:
        return False

    # base case 2: if the node's value is what we are looking for
    if curr.value == needle:
        return True

    # # traversal
    # if current node is less than target then we go right down the tree
    if curr.value < needle:
        return search(curr.right, needle)

    # otherwise go left down the tree
    return search(curr.left, needle)


def dfs(head: BinaryNode, needle: int) -> bool:
    return search(head, needle)
