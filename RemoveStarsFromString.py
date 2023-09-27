"""
https://leetcode.com/problems/removing-stars-from-a-string/

You are given a string s, which contains stars *.

In one operation, you can:
    * Choose a star in s.
    * Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

Note:
    * The input will be generated such that the operation is always possible.
    * It can be shown that the resulting string will always be unique.
"""


class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        # initialise an empty stack to store letters
        stack = []

        # iterate through each character in the input string
        for char in s:

            # if the character is a star then remove the previously added letter
            if char == "*":
                stack.pop()

            # otherwise, add letter to the stack
            else:
                stack.append(char)

        # convert stack to a string and return
        return "".join(stack)






sol = Solution()

print(sol.removeStars(s="leet**cod*e"))  # expected output: "lecoe"
print(sol.removeStars(s="erase*****"))  # expected output: ""
