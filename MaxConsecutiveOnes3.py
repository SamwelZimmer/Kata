"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip
at most k 0's.
"""


class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # initialise a pointer acting as the left of a sliding window
        left = 0

        # variables to store number of flipped values and the longest streak
        flipped, max_ones = 0, 0

        # iterate through the array with the pointer acting as the right of the sliding window
        for right in range(len(nums)):

            # if the value is a zero then it needs to be flipped and added to the count, otherwise nothing
            flipped += 1 ^ nums[right]

            # if number of flipped values exceeds the given k value
            if flipped > k:

                # change the flipped counter to account for the item leaving window
                flipped -= 1 ^ nums[left]

                # shift the left side of the window
                left += 1

            # otherwise, update the maximum number of consecutive values
            else:
                max_ones = max(max_ones, right - left + 1)

        return max_ones


sol = Solution()

print(sol.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
print(sol.longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
