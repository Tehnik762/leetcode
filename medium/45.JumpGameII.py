# You are given a 0-indexed array of integers nums of length n.
# You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i.
# In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1].
# The test cases are generated such that you can reach nums[n - 1].
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l > 1:
            res = {}
            for i in range(0, l):
                step = nums[i]
                while step > 0:
                    t = step + i
                    if t not in res.keys():
                        if i == 0:
                            res[t] = 1
                        else:
                            res[t] = res[i]+1
                    else:
                        pass
                    if t>= l-1:
                        return res[t]
                    step -= 1
        else:
            return 0

