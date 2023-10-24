"""
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()

        curr = dummy
        while list1 and list2:

            # if first list value smaller than second list
            if list1.val < list2.val:

                # add value to the output list
                curr.next = list1

                # move up the first list
                list1 = list1.next

            # if seconds list value smaller or equal to first list value
            else:

                # add value to the output list
                curr.next = list2

                # move up the first list
                list2 = list2.next

            # move up the list
            curr = curr.next

        # if either of the list is not empty, add to end of output list
        if list1:
            curr.next = list1

        elif list2:
            curr.next = list2

        # return output linked list
        return dummy.next


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

# expected 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
print_list(solution.mergeTwoLists(
    list1=list_to_listnode([1, 2, 4]),
    list2=list_to_listnode([1, 3, 4, 8]))
)

# expected: None
print_list(solution.mergeTwoLists(
    list1=list_to_listnode([]),
    list2=list_to_listnode([]))
)

# expected: 0 -> None
print_list(solution.mergeTwoLists(
    list1=list_to_listnode([]),
    list2=list_to_listnode([0]))
)
