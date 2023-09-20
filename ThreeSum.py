"""
ThreeSum.py

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
        LeetCode takes it but it is kinda outputting in tuples
        e.g. [(0, -1, 1)] rather than [[0, -1, 1]]
        """

        res = set()

        for i, x in enumerate(nums):

            hashmap = {}
            for j, y in enumerate(nums[i + 1:]):
                required = -(x + y)

                if required in hashmap:
                    res.add(tuple(sorted([x, y, required])))

                hashmap[y] = j

        return list(res)

    def withPointers(self, nums):

        # init output list
        res = []

        # sort the array
        nums.sort()

        # loop through array and set static value, x
        for i, x in enumerate(nums):

            # if not first value in array and same value as before skip to next iteration
            if i > 0 and x == nums[i - 1]:
                continue

            # create two pointers
            left, right = i + 1, len(nums) - 1

            # iterate so long as pointers don't cross
            while left < right:
                y, z = nums[left], nums[right]

                # if sum larger than zero then move right pointer to decrease z
                if x + y + z > 0:
                    right -= 1

                # if sum smaller than zero then move left pointer to increase y
                elif x + y + z < 0:
                    left += 1

                # if sum is satisfied then append to output list
                else:
                    res.append([x, y, z])

                    # I don't really get the bit below -> something to do with making more lists
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res


sol = Solution()

print(sol.withPointers([-1, 0, 1, 2, -1, -4]))  # expected output => [[-1,-1,2],[-1,0,1]]
"""
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""

# print(sol.threeSum([0, 1, 1]))  # expected output => []
# print(sol.threeSum([0, 0, 0]))  # expected output => [[0, 0, 0]]
