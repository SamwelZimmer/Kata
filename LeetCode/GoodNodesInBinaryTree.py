"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X
there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "Node(" + str(self.val) + ")"


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def walk(node, max_val):

            # base case
            if not node:
                return 0

            # check if node is good or not
            count = 1 if node.val >= max_val else 0

            # update maximum value
            max_val = max(max_val, node.val)

            # recurse down the tree and update number of 'good' nodes
            count += walk(node.left, max_val)
            count += walk(node.right, max_val)

            return count

        return walk(root, root.val)


def construct_tree(lst, index):
    if index < len(lst) and lst[index] is not None:
        node = TreeNode(lst[index])
        node.left = construct_tree(lst, 2*index + 1)
        node.right = construct_tree(lst, 2*index + 2)
        return node
    return None


sol = Solution()
print(sol.goodNodes(root=construct_tree([3, 1, 4, 3, None, 1, 5], 0)))      # expected: 4
print(sol.goodNodes(root=construct_tree([3, 3, None, 4, 2], 0)))            # expected: 3
print(sol.goodNodes(root=construct_tree([1], 0)))                           # expected: 1
