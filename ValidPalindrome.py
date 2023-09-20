"""
ValidPalindrome.py

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers

Given a string s, return true if it is a palindrome, or false otherwise
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        """This method uses two pointers rather than just checking the list is same as its reverse"""

        # convert to only lowercase letters
        clean = [char.lower() for char in s if char.isalnum()]

        # initialise the pointers
        left, right = 0, len(clean) - 1

        # iterate until pointers meet
        while left < right:

            print(clean[left], clean[right])

            # if left and right are not equal then not palindrome
            if clean[left] != clean[right]:
                return False

            # update pointers
            left += 1
            right -= 1

        return True


sol = Solution()

string = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(string))  # should return True as "amanaplanacanalpanama" is valid

string = "race a car"
print(sol.isPalindrome(string))

string = " "
print(sol.isPalindrome(string))

string = "0P"
print(sol.isPalindrome(string))
