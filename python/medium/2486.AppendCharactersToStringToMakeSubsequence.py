# You are given two strings s and t consisting of only lowercase
# English letters.
#
# Return the minimum number of characters that need to be appended to
# the end of s so that t becomes a subsequence of s.
#
# A subsequence is a string that can be derived from another string
# by deleting some or no characters without changing the order of the
# remaining characters.

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l_s = len(s)
        l_t = len(t)
        left, right = 0, 0
        pos = 0
        while left < l_s:
            if right >= l_t:
                break
            if s[left] == t[right]:
                left += 1
                right += 1
                pos += 1
            elif s[left] != t[right]:
                left += 1
        return l_t - pos



