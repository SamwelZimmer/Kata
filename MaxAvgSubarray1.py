"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        # set the initial value to be sum of the first window position
        window_sum = float(sum(nums[0:k]))

        # the variable to store the greatest sum value
        max_sum = window_sum

        # the start and end positions of the sliding window
        start_idx, end_idx = 0, k

        # iterate until the window reaches end of the array
        while end_idx < len(nums):

            # subtract the previous value
            window_sum -= nums[start_idx]

            # add the next value
            window_sum += nums[end_idx]

            # replace the largest value with new sum if it appropriate
            max_sum = max(window_sum, max_sum)

            # slide move the window
            start_idx += 1
            end_idx += 1

        # the greatest average is the sum divided by the number of elements
        return float(max_sum / k)

    def slowerSolution(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        """This method works but meets a runtime error. Could be due to calculating the sum at each window position"""

        # creating length variable as it is required often in the code
        length = len(nums)

        # if window smaller than array, return average of array
        if length <= k:
            return float(sum(nums)) / length

        # variable to store largest value - initialise as sum of first window
        max_avg = float(sum(nums[0:k])) / k

        # iterate through value with a sliding window of width k, which stops when window can't go further
        for i in range(length - k + 1):

            # make variable for the average to avoid calculating twice
            avg = float(sum(nums[i: i + k])) / k

            # replace largest value if applicable
            max_avg = max(max_avg, avg)

        return max_avg


sol = Solution()

print(sol.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
print(sol.findMaxAverage(nums=[5], k=1))
print(sol.findMaxAverage(nums=[9, 7, 3, 5, 6, 2, 0, 8, 1, 9], k=6))
print(sol.findMaxAverage(nums=[4, 0, 4, 3, 3], k=5))
