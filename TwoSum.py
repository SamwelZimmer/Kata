"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

class Solution(object):
    def twoSumSlow(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """O(n**2) time"""
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """O(n) time and memory"""

        # init empty map
        hashmap = {}

        # loop through all nums
        for i, num in enumerate(nums):

            # get the value needed to satisfy the sum
            required = target - num

            # check if this value is in the hashmap
            if required in hashmap:

                # return the indices as a list
                return [hashmap[required], i]

            # add all previously seen values to the hashmap
            hashmap[num] = i





sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9))  # [0, 1]

print(sol.twoSum([3, 2, 4], 6))  # [1, 2]

print(sol.twoSum([3, 3], 6))  # [0, 1]
