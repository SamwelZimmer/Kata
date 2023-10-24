"""
https://leetcode.com/problems/leaf-similar-trees/

Consider all the leaves of a binary tree, from left to right order,
the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if the two given trees with head nodes root1 and root2 are leaf-similar.
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "Node(" + str(self.val) + ")"


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        # recursive traversal function
        def walk(node, leaves):

            # base case: not at a node
            if not node:
                return

            # at a leaf node if no left or right children, append node's value to array
            if (node.right is None) and (node.left is None):
                leaves.append(node.val)

            # traverse the tree
            walk(node.left, leaves)
            walk(node.right, leaves)

        # init empty lists to store the leaf node values
        leaves_list1 = []
        leaves_list2 = []

        # traverse both trees
        walk(root1, leaves_list1)
        walk(root2, leaves_list2)

        # will return true if trees are 'leaf similar'
        return leaves_list1 == leaves_list2


def construct_tree(lst, index):
    if index < len(lst) and lst[index] is not None:
        node = TreeNode(lst[index])
        node.left = construct_tree(lst, 2*index + 1)
        node.right = construct_tree(lst, 2*index + 2)
        return node
    return None


sol = Solution()
print(sol.leafSimilar(
    root1=construct_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4], 0),
    root2=construct_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8], 0)
))      # expected: True
print(sol.leafSimilar(root1=construct_tree([1, 2, 3], 0), root2=construct_tree([1, 3, 2], 0)))      # expected: False
