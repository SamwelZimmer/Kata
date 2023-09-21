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

        # init empty result list
        res = []

        # loop through the largest word
        for i in range(max(len(word1), len(word2))):

            # if within range of first word add it to list
            if i < len(word1):
                res.append(word1[i])

            # if within range of second word add it to list
            if i < len(word2):
                res.append(word2[i])

        # convert list to string and return
        return "".join(res)




sol = Solution()

print(sol.mergeAlternately("abc", "pqr"))  # expected -> "apbqcr"

print(sol.mergeAlternately("ab", "pqrs"))  # expected -> "apbqrs"

print(sol.mergeAlternately("abcd", "pq"))  # expected -> "apbqcd"
