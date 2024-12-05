# Given an integer array nums, move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                l -= 1
            else:
                i += 1

