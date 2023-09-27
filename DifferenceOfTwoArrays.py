"""
https://leetcode.com/problems/find-the-difference-of-two-arrays/

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

* answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
* answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.
"""


class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        # convert both lists into sets
        nums1, nums2 = set(nums1), set(nums2)

        # return list of the differences in these sets
        return [list(nums1.difference(nums2)), list(nums2.difference(nums1))]


sol = Solution()

print(sol.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))  # expected output: [[1,3], [4,6]]
print(sol.findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]))  # expected output: [[3], []]
