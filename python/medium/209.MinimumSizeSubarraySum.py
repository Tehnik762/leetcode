# Given an array of positive integers nums and a positive integer target, return
# the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.
#
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        maxim = max(nums)
        if maxim >= target:
            return 1
        start = 0
        res = []
        end = 1
        slide = 0
        subarr = nums[0]
        while end < len(nums):
            subarr = subarr + nums[end]
            if end == 1:
                slide = 2
            else:
                slide += 1
            while subarr >= target:
                res.append(slide)
                subarr -= nums[start]
                start += 1
                slide -= 1
            end += 1
        if len(res) > 0:
            return min(res)
        else:
            return 0
