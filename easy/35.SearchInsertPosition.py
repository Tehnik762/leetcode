# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index
# where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if target <= nums[0]:
            return 0
        if target > nums[l-1]:
            return l
        # search = int((target / (nums[l-1] - nums[0]))*l)
        search = (l-1)//2
        search_lib = []
        while True:
            if search not in search_lib:
                search_lib.append(search)
                if target == nums[search]:
                    return search
                elif target < nums[search]:
                    search = int(search/2)
                else:
                    search = int((l - search)/2)+search
            else:
                search = search_lib.pop()
                if target > nums[search]:
                    while target > nums[search+1]:
                        search += 1
                    return search + 1
                elif target < nums[search]:
                    if target > nums[search-1]:
                        return search
                    else:
                        return search - 1
                else:
                    return search - 1

