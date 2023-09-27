"""
https://leetcode.com/problems/determine-if-two-strings-are-close/

Two strings are considered close if you can attain one from the other using the following operations:

* Operation 1: Swap any two existing characters.
    For example, abcde -> aecdb
* Operation 2: Transform every occurrence of one existing character into another existing character, and do the same
with the other character.
    For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
"""


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        # convert words to lists
        word1, word2 = list(word1), list(word2)

        # hashmaps counting the character occurrences
        word1_map, word2_map = {}, {}

        # cannot be close if different lengths
        if len(word1) != len(word2):
            return False

        # fill hashmaps for counting occurrences of each character
        for i in range(len(word1)):

            # if items exists then increase count by one, else set count to 1
            word1_map[word1[i]] = word1_map.get(word1[i], 0) + 1
            word2_map[word2[i]] = word2_map.get(word2[i], 0) + 1

        # words are similar if you can reorder them
        if word1_map == word2_map:
            return True

        # if the frequencies of the letters in each word are the same and share the same characters
        if sorted(word1_map.values()) == sorted(word2_map.values()) and set(word1_map.keys()) == set(word2_map.keys()):
            return True

        # if neither condition is true then the words are not similar
        return False


sol = Solution()

print(sol.closeStrings(word1="abc", word2="bca"))  # expected: true
print(sol.closeStrings(word1="a", word2="aa"))  # expected: false
print(sol.closeStrings(word1="cabbba", word2="abbccc"))  # expected: true
print(sol.closeStrings(word1="uau", word2="ssx"))  # expected: false


