"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        def check_divisor(string, divisor):

            # if remainder when dividing, cannot be the answer
            if len(string) % len(divisor) != 0:
                return False

            # get number of times divisor divides into string
            multiple = int(len(string) / len(divisor))

            # if this divisor multiples into the string then it is valid
            return divisor * multiple == string

        # assuming length str2 < str1
        prefix = str2

        # check if str2 divides into str1
        if check_divisor(str1, prefix):
            return prefix

        # iterate through each character in smaller string
        for i in range(len(str2)):

            # this would otherwise make prefix an empty string ("")
            if i == 0:
                continue

            # continuously reduce the size of the prefix
            prefix = str2[:-i]

            # if prefix divides into both strings this is the answer
            if check_divisor(str1, prefix) and check_divisor(str2, prefix):
                return prefix

        # if no divisor found return empty string
        return ""


sol = Solution()

print(sol.gcdOfStrings("ABCABC", "ABC"))  # expected output -> "ABC"
print(sol.gcdOfStrings("ABABAB", "ABAB"))  # expected output -> "AB"
print(sol.gcdOfStrings("LEET", "CODE"))  # expected output -> ""
