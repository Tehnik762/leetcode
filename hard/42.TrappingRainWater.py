# Given n non-negative integers representing an elevation map where
# the width of each bar is 1, compute how much water it can trap after raining.
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        res = 0
        if l > 2:
            left = height[0]
            maximum = max(height[2:])
            med = min(left, maximum)
            i = 1
            while i < l:
                if height[i] < left and height[i] < maximum:
                    res += med - height[i]
                if height[i] >= left:
                    left = height[i]
                    med = min(left, maximum)
                if height[i] >= maximum:
                    left = maximum
                    if i+1 < l:
                        next = i+1
                        maximum = max(height[next:])
                        med = min(left, maximum)
                i += 1
        return res

