"""
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# can't run this solution here, but it works for LeetCode


# definition for singly-linked list node.
class ListNode(object):
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # create variable to store the previous and current nodes
        prev = None
        curr = head

        # iterate until traversed to end of the list
        while curr is not None:

            # assign next node to variable
            nxt = curr.nxt

            # update to point to the previous node
            curr.nxt = prev

            # slide the prev variable up one position
            prev = curr

            # traverse one position
            curr = nxt

        # reassign the head pointer
        head = prev

        return head


def list_to_listnode(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.nxt = ListNode(val)
        current = current.nxt
    return dummy.nxt


def print_list(node):
    current = node
    while current is not None:
        print(current.val, end=" -> ")
        current = current.nxt
    print(None)  # Print None at the end to signify the end of the list


solution = Solution()
print_list(solution.reverseList(list_to_listnode([1, 2, 3, 4, 5])))
# print(solution.reverseList([1, 2]))
# print(solution.reverseList([]))
