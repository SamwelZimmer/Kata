"""
https://leetcode.com/problems/increasing-triplet-subsequence/

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and
nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # solution in O(n) in space and time

        n = len(nums)

        lowest_values, highest_values = [None] * n, [None] * n
        lowest_values[0], highest_values[-1] = nums[0], nums[-1]

        for i in range(n - 1):
            lowest_values[i + 1] = min(lowest_values[i], nums[i + 1])

        for i in range(n - 1):
            highest_values[-i - 2] = max(highest_values[-i - 1], nums[-i - 2])

        for i in range(n):
            if lowest_values[i] < nums[i] < highest_values[i]:
                return True

        return False

    def betterSolution(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # initialise variables to store first and third values
        first, third = float("inf"), float("inf")

        # iterate through the numbers
        for second in nums:

            # if the middle value is less than the first, then left-most value should be reassigned
            if second <= first:
                first = second

            # if the middle value is more than the third, then right-most value should be reassigned
            elif second >= third:
                third = second

            # if previous conditions are satisfied then we have found a valid sequence
            else:
                return True

        return False


sol = Solution()

print(sol.betterSolution(nums=[1, 2, 3, 4, 5]))              # expected: True
print(sol.betterSolution(nums=[5, 4, 3, 2, 1]))              # expected: False
print(sol.betterSolution(nums=[2, 1, 5, 0, 4, 6]))           # expected: True
print(sol.betterSolution(nums=[20, 100, 10, 12, 5, 13]))     # expected: True
