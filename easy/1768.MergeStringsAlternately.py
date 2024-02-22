# You are given two strings word1 and word2. Merge the strings by adding
# letters in alternating order, starting with word1. If a string is longer
# than the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        return res