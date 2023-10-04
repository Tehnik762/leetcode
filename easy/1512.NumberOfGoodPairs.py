# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
#
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        origin_nums = {}

        for i in nums:
            if i in origin_nums.keys():
                origin_nums[i] += 1
            else:
                origin_nums[i] = 1
        res = 0
        for i in origin_nums.values():
            if i > 1:
                temp = i*(i-1)/2
                res += int(temp)
        return res
