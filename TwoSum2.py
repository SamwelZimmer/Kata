"""
TwoSum2.py

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such
that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""


class Solution(object):
    def twoSumSlow(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        This solution takes too long -> O(n**2)
        """

        for i in range(len(numbers)):
            left = numbers[i]
            for j in range(len(numbers)):
                right = numbers[j]
                if j > i and left + right == target:
                    return [i + 1, j + 1]

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        """This method uses two pointers"""

        # initialise a pointer at either end
        left, right = 0, len(numbers) - 1

        # iterate until pointers meet
        while left < right:

            # get the values at the pointers' indices
            x, y = numbers[left], numbers[right]

            # if sum is too large then must shift right pointer to decrease y
            if x + y > target:
                right -= 1

            # if sum is too large then must shift left pointer to increase x
            elif x + y < target:
                left += 1

            # if x + y = target then return their indices in requested format
            else:
                return [left + 1, right + 1]


sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9))  # 2 + 7 = 9 so indices are [1, 2]

print(sol.twoSum([2, 3, 4], 6))

print(sol.twoSum([-1, 0], -1))
