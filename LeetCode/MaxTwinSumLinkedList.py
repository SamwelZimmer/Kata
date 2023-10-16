"""
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of
the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2.
These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        # traverse entire list to get length
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next

        # if linked list is only of length two then can sum the node's values
        if length == 2:
            return head.val + head.next.val

        # a value to store the head of new linked list
        head_2 = None

        # traverse up to the midpoint
        count, curr = 1, head
        while count <= (length // 2):
            count += 1

            curr = curr.next

            # when midpoint is reached, break the chain and add to the new head pointer
            if count == length // 2:
                head_2 = curr.next
                curr.next = None

        # reverse the second chain
        prev, curr = None, head_2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head_2 = prev

        # traverse through both lists at same time and keep track of maximum sum
        max_sum = 0

        curr_1, curr_2 = head, head_2
        while curr_1:

            max_sum = max(curr_1.val + curr_2.val, max_sum)

            curr_1 = curr_1.next
            curr_2 = curr_2.next

        return max_sum


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
print(solution.pairSum(list_to_listnode([5, 4, 2, 1])))        # expected: 6
print(solution.pairSum(list_to_listnode([4, 2, 2, 3])))        # expected: 7
print(solution.pairSum(list_to_listnode([1, 100000])))         # expected: 100001
