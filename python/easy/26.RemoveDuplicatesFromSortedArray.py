# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once. The relative
# order of the elements should be kept the same. Then return the number of unique
# elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need
# to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique
# elements in the order they were present in nums initially. The remaining elements
# of nums are not important as well as the size of nums.
# Return k.
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = len(nums)
        temp = nums[0]
        unique = 1
        for i in range(1,l):
            if nums[i] == temp:
                nums[i] = "_"
            else:
                temp = nums[i]
                unique += 1
        nums.sort(key=lambda a: a == "_" )
        return unique

