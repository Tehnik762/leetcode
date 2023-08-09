#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative
from typing import List

#  first approach - too slow
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             x = nums.pop()
#             nums.insert(0, x)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l > 1 and k > 0:
            if l < k+1:
                k = k%l
            nums[:] = nums[-k::] + nums[:-k:]
