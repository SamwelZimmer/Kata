"""
You have a long flowerbed in which some plots are planted, and some are not. However, flowers cannot
be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        # initialise variable to store number of possible positions
        count = 0

        # iterate through each position in flower bed
        for i in range(len(flowerbed)):

            # if flowerbed has only one plot
            if len(flowerbed) == 1 and flowerbed[0] == 0:
                count += 1
                continue

            # if item at start of flowerbed is empty and nothing to its right
            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
                continue

            # if item at end of flowerbed is empty and nothing to its left
            if i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                count += 1
                continue

            # if a plot in flowerbed is empty and surrounded by empty plots then it's valid
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
                continue

        # return True if the number of possible positions is more (or equal) to input variable, n
        return count >= n


sol = Solution()

print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))  # expected output: true
print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 0, 1], n=2))  # expected output: true
print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))  # expected output: false
print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1, 0, 0], n=2))  # expected output: true
print(sol.canPlaceFlowers(flowerbed=[0], n=2))  # expected output: false



