"""
https://leetcode.com/problems/odd-even-linked-list/

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with
even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # if list is empty
        if not head or not head.next:
            return head

        # init variable to store last seen odd / even nodes
        odd = head
        even = odd.next

        # variable to store the first seen even node
        even_head = even

        # iterate until end of linked list
        while even and even.next:

            # traverse and connect the odd nodes
            odd.next = even.next
            odd = odd.next

            # traverse and connect the even nodes
            even.next = odd.next
            even = even.next

        # point from the end of the odd to start of even chain
        odd.next = even_head

        return head


def list_to_listnode(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_list(node):
    current = node
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print(None)  # Print None at the end to signify the end of the list


solution = Solution()
print_list(solution.oddEvenList(list_to_listnode([1, 2, 3, 4, 5])))  # expected 1 -> 3 -> 5 -> 2 -> 4
print_list(solution.oddEvenList(list_to_listnode([2, 1, 3, 5, 6, 4, 7])))  # expected 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
