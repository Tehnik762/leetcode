# Given two integer arrays nums1 and nums2, return an array of
# their intersection. Each element in the result must appear as
# many times as it shows in both arrays and you may return the result in any order.
#
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = self.makeADict(nums1)
        nums2_dict = self.makeADict(nums2)
        res_dict = {}
        for pos in nums1_dict:
            if pos in nums2_dict.keys():
                res_dict[pos] = min(nums1_dict[pos], nums2_dict[pos])
        res = []
        for pos in res_dict:
            for i in range(res_dict[pos]):
                res.append(pos)
        return res

    def makeADict(self, num_list: List[int]):
        res_dict = {}
        for num in num_list:
            if num in res_dict.keys():
                res_dict[num] += 1
            else:
                res_dict[num] = 1
        return res_dict
