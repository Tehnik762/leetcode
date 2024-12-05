# You are given an integer array height of length n. There are n
# vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
from typing import List
import time
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) > 2:
            all = []
            left = 0
            right = len(height) - 1
            mmm = 0
            while left < right:
                temp_s = min(height[left], height[right])*(right-left)
                if temp_s > mmm:
                    mmm = temp_s
                if height[right] < height[left]:
                    right -= 1
                else:
                    left += 1
            return mmm
        elif len(height) == 2:
            return min(height)
        else:
            return 0
