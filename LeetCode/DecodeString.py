"""
https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly
k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed,
etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those
repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # initialise an empty stack
        stack = []

        # loop through each character in the input string
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                # to store the items inside the brackets
                internal = ""

                # iterate until there is an opening bracket at end of the stack
                while stack[-1] != "[":
                    internal = stack.pop() + internal

                # remove opening bracket
                stack.pop()

                # to store the multiplier
                multiplier = ""

                # if the stack is not empty and last item is a number
                while stack and stack[-1].isnumeric():
                    multiplier = stack.pop() + multiplier

                # multiply the internal string with the multiplier and add back onto the stack
                stack.append(int(multiplier) * internal)

        # return the stack as a string
        return "".join(stack)


sol = Solution()

print(sol.decodeString(s="3[a]2[bc]"))          # expected "aaabcbc"
print(sol.decodeString(s="3[a2[c]]"))           # expected "accaccacc"
print(sol.decodeString(s="2[abc]3[cd]ef"))      # expected "abcabccdcdcdef"
