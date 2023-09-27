"""
https://leetcode.com/problems/find-pivot-index/

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of
all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # initialise variables to store the left and right sums
        left_sum, right_sum = 0, sum(nums) - nums[0]

        # iterate through the input array
        for i in range(len(nums)):

            # if the sums either side are equal then this is the first pivot index
            if left_sum == right_sum:
                return i

            # increase the left sum
            left_sum += nums[i]

            # reduce the right sum, and equal to 0 when at end of the array
            right_sum = 0 if i == len(nums) - 1 else right_sum - nums[i + 1]

        # if no pivot found return -1
        return -1


sol = Solution()

print(sol.pivotIndex(nums=[1, 7, 3, 6, 5, 6]))  # expected 3
print(sol.pivotIndex(nums=[1, 2, 3]))  # expected -1
print(sol.pivotIndex(nums=[2, 1, -1]))  # expected 0
print(sol.pivotIndex(nums=[-1, -1, 0, 1, 1, 0]))  # expected 5
