"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""


# definition for singly-linked list node.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # variable to store the number of nodes in the list
        count = 0

        # traverse the list to get the length
        curr = head
        while curr:
            curr = curr.next
            count += 1

        # the case where only one node
        if count == 1:
            return None

        # get the index of the middle node
        middle_index = count // 2

        # create a variable to store the count
        count = 0

        # # traverse to this middle node
        # keep track of the current and previous nodes
        prev = None
        curr = head

        # iterate until end of list or meeting the middle node
        while curr and count < middle_index:
            count += 1
            prev = curr
            curr = curr.next

        # skip over the current node to 'delete' it
        prev.next = curr.next

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
print_list(solution.deleteMiddle(list_to_listnode([1, 3, 4, 7, 1, 2, 6])))
print_list(solution.deleteMiddle(list_to_listnode([1, 2, 3, 4])))
print_list(solution.deleteMiddle(list_to_listnode([2, 1])))
print_list(solution.deleteMiddle(list_to_listnode([1])))

