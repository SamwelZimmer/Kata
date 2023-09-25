"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # a list of all possible vowels
        vowel_list = ['a', 'e', 'i', 'o', 'u']

        # initialise the left and right positions of the sliding window
        left, right = 0, k

        # convert the string into a list
        s = list(s)

        # get number of vowels in first possible window
        vowels = len([char for char in s[left:right] if char in vowel_list])

        # initialise a variable to store greatest number of vowels
        max_vowels = vowels

        # iterate until the window meets the end of the list
        while right < len(s):

            # if value which is leaving the window is a vowel then reduce the vowel count
            if s[left] in vowel_list:
                vowels -= 1

            # if value which is entering the window is a vowel then increase the vowel count
            if s[right] in vowel_list:
                vowels += 1

            # overwrite the greatest vowel count if the current window has more vowels than previous maximum
            max_vowels = max(max_vowels, vowels)

            # slide the window
            left, right = left + 1, right + 1

        return max_vowels


sol = Solution()

print(sol.maxVowels(s="abciiidef", k=3))  # expected output: 3
print(sol.maxVowels(s="aeiou", k=2))  # expected output: 2
print(sol.maxVowels(s="leetcode", k=3))  # expected output: 2
