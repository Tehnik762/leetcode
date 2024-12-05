# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l < 2:
            return l
        else:
            cache = {}
            cache[s[0]] = 1
            left = 0
            right = 1
            res = [1]
            while right < l:
                if s[right] not in cache.keys():
                    cache[s[right]] = 1
                    right += 1
                else:
                    if cache[s[right]] == 0 and s[left] != s[right]:
                        cache[s[right]] = 1
                        right += 1
                    else:
                        res.append(right-left)
                        left = s.index(s[right], left) + 1
                        cache = {}
                        cache[s[left]] = 1
                        right = left + 1
            res.append(right - left)
            return max(res)

