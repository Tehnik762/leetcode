# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
#
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.
#
from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        start = nums[0]
        check = nums[1]
        i = 2
        if start == check:
            while start == check and i < n:
                check = nums[i]
                i += 1
        if start > check:
            trend = "down"
        elif check > start:
            trend = "up"

        for step in range(i, n):
            temp = nums[step]
            if temp != check:
                start = check
                check = nums[step]
                if start > check and trend != "down":
                    return False
                elif check > start and trend != "up":
                    return False

        return True

