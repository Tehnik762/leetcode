# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
#
# Return any array that satisfies this condition.
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even =[]
        odd = []
        for i in nums:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even+odd

