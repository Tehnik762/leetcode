# You are given an integer array nums. You are initially positioned at
# the array's first index, and each element in the array represents
# your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        j = l - 1
        i = l - 2
        while i >=0:
            step = 0
            while step<=nums[i]:
                s = i+step
                print(f"i - {i}, step - {step}, nums[{i}] - {nums[i]} s - {s}, j - {j}")
                if s == j:
                    j = i
                    break
                step += 1
            i -= 1
        if j == 0:
            return True
        else:
            return False

