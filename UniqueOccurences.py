"""
https://leetcode.com/problems/unique-number-of-occurrences/

Given an array of integers arr, return true if the number of occurrences of each
value in the array is unique or false otherwise.
"""


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # initialise hashmap to store the count of each value
        occurrence_dict = {}

        # iterate through input array
        for i in range(len(arr)):

            # if items exists then increase count by one, else set count to 1
            occurrence_dict[arr[i]] = occurrence_dict.get(arr[i], 0) + 1

        # if the length of the set is same as the list then each value is unique
        return len(occurrence_dict.values()) == len(set(occurrence_dict.values()))


sol = Solution()

print(sol.uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3]))  # expected: true
print(sol.uniqueOccurrences(arr=[1, 2]))  # expected: false
print(sol.uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))  # expected: true
