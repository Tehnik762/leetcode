# Given an array of strings strs, group the anagrams together. You can return the answer
# in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for one in strs:
            liter = list(one)
            liter.sort()
            liter = "".join(liter)
            if liter in res.keys():
                res[liter].append(one)
            else:
                res[liter] = [one]

        return list(res.values())

