"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of
candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        # get the max number of candies
        largest = max(candies)

        # loop through each kid and see if they would have the most if also had extraCandies
        return [candy + extraCandies >= largest for candy in candies]


sol = Solution()

print(sol.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))  # expected: [true, true, true, false, true]
print(sol.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))  # expected: [true, false, false, false, false]
print(sol.kidsWithCandies(candies=[12, 1, 12], extraCandies=10))  # expected: [true, false, true]
