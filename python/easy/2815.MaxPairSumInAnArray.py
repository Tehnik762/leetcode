# You are given a 0-indexed integer array nums. You have to find the
# maximum sum of a pair of numbers from nums such that the maximum
# digit in both numbers are equal.
#
# Return the maximum sum or -1 if no such pair exists.

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        out = -1
        num_table = {
            "0": [],
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [],
            "9": [],
        }
        for i in nums:
            x = str(i)
            if len(x) < 2:
                num_table[x].append(i)
            else:
                m = max(x)
                x = str(m)
                num_table[x].append(i)
        for i in range(9, -1, -1):
            i = str(i)
            if len(num_table[i]) > 1:
                num_table[i].sort()
                a = num_table[i].pop()
                b = num_table[i].pop()
                if a + b > out:
                    out = a + b

        return out


