# Write a function to find the longest common prefix string
# amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        l = len(strs)
        for i in range(1, l):
            l_pr = len(prefix)
            l_i = len(strs[i])
            if l_pr < 1:
                break
            if l_i < l_pr:
                prefix = prefix[:l_i]
                l_pr = len(prefix)
            new_prefix = ""
            for j in range(0, l_pr):
                if prefix[j] == strs[i][j]:
                    new_prefix += prefix[j]
                else:
                    break
            prefix = new_prefix
        return prefix
