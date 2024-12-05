# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1]*l
        l_products = []
        r_products = [1]*l
        temp_l = 1
        temp_r = 1
        zero = nums.count(0)


        for i in range(0, l):
            l_products.append(temp_l)
            temp_l *= nums[i]


        for i in range(l-1, -1, -1):
            r_products[i] = temp_r
            temp_r *= nums[i]


        for i in range(0, l):
            if zero > 0:
                if nums[i] != 0:
                    res[i] = 0
                else:
                    res[i] = (l_products[i] * r_products[i])
            else:
                res[i] = (l_products[i] * r_products[i])


        return res

