"""
three types of Depth First Search (DFS) binary tree traversals
"""

from typing import List


class BinaryNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def pre_order_walk(self, curr: BinaryNode, path: List[int]) -> List[int]:

        # base case is when there is no node
        if not curr:
            return path

        # pre-recursion
        path.append(curr.value)

        # recurse
        self.pre_order_walk(curr.left, path)
        self.pre_order_walk(curr.right, path)

        # post-recursion
        return path

    def pre_order_traversal(self, head: BinaryNode) -> List[int]:
        return self.pre_order_walk(head, [])

    def in_order_walk(self, curr: BinaryNode, path: List[int]) -> List[int]:

        # base case is when there is no node
        if not curr:
            return path

        # # recurse
        # walk left until we cannot go further
        self.in_order_walk(curr.left, path)

        # visit the node
        path.append(curr.value)

        # walk right until we cannot go further
        self.in_order_walk(curr.right, path)

        # post-recursion
        return path

    def in_order_traversal(self, head: BinaryNode) -> List[int]:
        return self.in_order_walk(head, [])

    def post_order_walk(self, curr: BinaryNode, path: List[int]) -> List[int]:

        # base case is when there is no node
        if not curr:
            return path

        # # recurse
        # walk left until we cannot go further
        self.post_order_walk(curr.left, path)

        # walk right until we cannot go further
        self.post_order_walk(curr.right, path)

        # post-recursion
        path.append(curr.value)
        return path

    def post_order_traversal(self, head: BinaryNode) -> List[int]:
        return self.post_order_walk(head, [])


bt = BinaryTree()
bt.root = BinaryNode(1, BinaryNode(2, BinaryNode(4), BinaryNode(5)), BinaryNode(3))

print(bt.pre_order_traversal(bt.root))   # [1, 2, 4, 5, 3]
print(bt.in_order_traversal(bt.root))    # [4, 2, 5, 1, 3]
print(bt.post_order_traversal(bt.root))  # [4, 5, 2, 3, 1]
