"""
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Follow up: Could you minimize the total number of operations done?
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # initialise two pointers
        left, right = 0, 0

        # iterate until right pointer get to end of list
        while right < len(nums):

            # if left pointer at a zero and right is at a value, swap them
            if nums[left] == 0 and nums[right] != 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

            # only stop left pointer when meeting a zero
            if nums[left] != 0:
                left += 1

            # continuously move right pointer
            right += 1


sol = Solution()

print(sol.moveZeroes(nums=[0, 1, 0, 3, 12]))  # expected output -> [1, 3, 12, 0, 0]
print(sol.moveZeroes(nums=[0]))  # expected output -> [0]
