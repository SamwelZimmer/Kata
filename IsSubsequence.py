"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
of "abcde" while "aec" is not).

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one
to see if t has its subsequence. In this scenario, how would you change your code?
"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # initialise pointer
        p = 0

        # initialise empty array to store matching letters
        found = []

        # if substring empty then always true
        if s == "":
            return True

        # if main string empty then false (unless substring also empty)
        if t == "":
            return False

        # iterate through each character in main string
        for char in t:

            # if the letter is same as the letter pointed to in subarray then add to list and shift pointer
            if char == s[p]:
                found.append(char)
                p += 1

            # once the list of matching letters is same as substring then return true
            if "".join(found) == s:
                return True

        # if matching letters never equals the substring then return false
        return False


sol = Solution()

print(sol.isSubsequence(s="abc", t="ahbgdc"))  # expected: true
print(sol.isSubsequence(s="axc", t="ahbgdc"))  # expected: false
