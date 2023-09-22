"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # initialise a pointer at either end of the list
        left, right = 0, len(height) - 1

        # initialise a variable to store the largest value
        max_water = 0

        # stop iterating when pointers meet
        while left < right:

            # calc amount of water (the smallest height x distance between them)
            water = min(height[left], height[right]) * (right - left)

            # update the largest value
            if water > max_water:
                max_water = water

            # if right wall is smaller than left, shift right pointer down
            if height[left] > height[right]:
                right -= 1

            # if left wall is shorter, or walls are of equal height, shift up the left pointer
            else:
                left += 1

        # return the largest volume found
        return max_water





sol = Solution()

print(sol.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))  # expected output: 49
print(sol.maxArea(height=[1, 1]))  # expected output: 1

