"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        # list of vowels
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

        # initialise two pointers
        left, right = 0, len(s) - 1

        # convert string to array
        chars = list(s)

        # iterate until the two pointers meet
        while left < right:

            # if left is vowel but not right, pause moving left until right is also vowel
            if chars[left] in vowels and chars[right] not in vowels:
                right -= 1
                continue

            # if right is vowel but not left, pause moving right until left is also vowel
            if chars[right] in vowels and chars[left] not in vowels:
                left += 1
                continue

            # if both right and left are vowels then swap their values
            if chars[right] in vowels and chars[left] in vowels:
                temp = chars[left]
                chars[left] = chars[right]
                chars[right] = temp

            # shift the pointers
            left += 1
            right -= 1

        # convert the altered array to a string and return
        return "".join(chars)


sol = Solution()

print(sol.reverseVowels(s="hello"))  # expected output: "holle"
print(sol.reverseVowels(s="leetcode"))  # expected output: "leotcede"

