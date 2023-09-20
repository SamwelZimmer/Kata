"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """


sol = Solution()

print(sol.mergeAlternately("abc", "pqr"))  # expected -> "apbqcr"

print(sol.mergeAlternately("ab", "pqrs"))  # expected -> "apbqrs"

print(sol.mergeAlternately("abcd", "pq"))  # expected -> "apbqcd"
