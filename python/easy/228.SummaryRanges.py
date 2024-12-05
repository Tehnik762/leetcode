# You are given a sorted unique integer array nums.
#
# A range [a,b] is the set of all integers from a to b (inclusive).
#
# Return the smallest sorted list of ranges that cover all the numbers
# in the array exactly. That is, each element of nums is covered by
# exactly one of the ranges, and there is no integer x such that x is
# in one of the ranges but not in nums.
#
# Each range [a,b] in the list should be output as:
#
# "a->b" if a != b
# "a" if a == b
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        res =[]
        temp = nums[0]
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i]-temp == 1:
                temp = nums[i]
            elif start == temp:
                text = str(start)
                start = nums[i]
                temp = nums[i]
                res.append(text)
            else:
                text = str(start)+"->"+str(temp)
                start = nums[i]
                temp = nums[i]
                res.append(text)
        if start == temp:
            text = str(start)
            res.append(text)
        else:
            text = str(start) + "->" + str(temp)
            res.append(text)

        return res




