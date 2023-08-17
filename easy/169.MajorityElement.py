# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋
# times. You may assume that the majority element always exists in the array.
#

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res ={}
        n = len(nums)
        for i in nums:
            if res.get(i):
                res[i] += 1
            else:
                res[i] = 1
            if res[i] > n/2:
                return i

