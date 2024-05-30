# Given two strings needle and haystack, return the index of
# the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l_needle = len(needle)
        l_haystack = len(haystack)

        if l_haystack == l_needle:
            if needle == haystack:
                return 0
            else:
                return -1
        if l_needle > l_haystack:
            return -1
        stop = l_haystack - l_needle
        for i, step in enumerate(haystack):
            if i > stop:
                break
            if step == needle[0]:
                left = i
                right = 0
                while right < l_needle-1:
                    if haystack[left] != needle[right]:
                        break
                    else:
                        left += 1
                        right += 1
                if haystack[left] == needle[right]:
                    return i

        return -1
