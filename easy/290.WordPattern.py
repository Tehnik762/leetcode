# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between
# a letter in pattern and a non-empty word in s.s

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        l_pattern = len(pattern)
        if l_pattern != len(words):
            return False
        if len(set(words)) != len(set(pattern)):
            return False
        d = {}
        pos = 0
        for i in pattern:
            if i in d.keys():
               if d[i] != words[pos]:
                   return False
            else:
                d[i] = words[pos]
            pos += 1
        return True
