"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # sort the input array into ascending order
        nums.sort()

        # initialise a pointer at either side of the list
        left, right = 0, len(nums) - 1

        # initialise a variable to store the number of operations
        counter = 0

        # iterate until the pointers meet
        while left < right:

            # get the values at the pointer positions
            x, y = nums[left], nums[right]

            # if sum of the two values is less than target then need to shift right pointer to the left
            if x + y < k:
                left += 1

            # if sum of the two values is more than target then need to shift left pointer to the right
            elif x + y > k:
                right -= 1

            # if values sum to the target then add to the count and move both pointers toward each other
            else:
                counter += 1
                left += 1
                right -= 1

        # return the counter variable
        return counter




sol = Solution()

print(sol.maxOperations(nums=[1, 2, 3, 4], k=5))  # expected: 2
print(sol.maxOperations(nums=[3, 1, 3, 4, 3], k=6))  # expected: 1

