# Given a string s, find the first non-repeating character in it
# and return its index. If it does not exist, return -1.
#

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ind = -1
        t_dict = {}
        for i in s:
            if i in t_dict.keys():
                t_dict[i] += 1
            else:
                t_dict[i] = 1
        for i, position in enumerate(s):
            if t_dict[position] == 1:
                return i
        return ind

