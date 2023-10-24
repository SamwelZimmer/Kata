"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the
farthest leaf node.
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "Node(" + str(self.val) + ")"


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # no depth if no root node
        if not root:
            return 0

        # function used for recursively traversing the tree
        def walk(node: TreeNode):

            # base case: not at a node
            if not node:
                return 0

            # at each node move both left and right
            left_depth = walk(node.left)
            right_depth = walk(node.right)

            # get the largest depth that either side has reached (plus 1 to account for root node)
            return max(left_depth, right_depth) + 1

        # call the recursive function
        return walk(root)


def construct_tree(lst, index):
    if index < len(lst) and lst[index] is not None:
        node = TreeNode(lst[index])
        node.left = construct_tree(lst, 2*index + 1)
        node.right = construct_tree(lst, 2*index + 2)
        return node
    return None


sol = Solution()
print(sol.maxDepth(root=construct_tree([3, 9, 20, None, None, 15, 7], 0)))      # expected: 3
print(sol.maxDepth(root=construct_tree([1, None, 2], 0)))                       # expected: 2
