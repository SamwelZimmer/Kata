"""
https://leetcode.com/problems/reverse-words-in-a-string/

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only
have a single space separating the words. Do not include any extra spaces.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = []
        for item in s.split(" ")[::-1]:
            if item != "":
                output.append(item)

        return " ".join(output)


sol = Solution()

print(sol.reverseWords(s="the sky is blue"))    # expected: "blue is sky the"
print(sol.reverseWords(s="  hello world  "))    # expected: "world hello"
print(sol.reverseWords(s="a good   example"))   # expected: "example good a"
