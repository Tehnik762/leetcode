# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by
# deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first = 0
        second = 0
        l_s = len(s)
        l_t = len(t)
        if l_t == 0:
            if l_s == 0:
                return True
            else:
                return False
        while second < l_t:
            if first >= l_s:
                return True
            if s[first] == t[second]:
                first += 1
            second += 1
        if first == second or first >= l_s:
            return True
        return False


