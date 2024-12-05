# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping
# intervals that cover all the intervals in the input.
#
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            previous_start, previous_end = merged[-1]


            if current_start <= previous_end:
                merged[-1][1] = max(previous_end, current_end)
            else:
                merged.append([current_start, current_end])

        return merged




b = Solution()

test = [
    [[1,3],[2,6],[8,10],[15,18]],
    [[1,4],[4,5]],
    [[1,4],[0,4]],
    [[1,4],[0,1]],
    [[1,4],[0,0]]
]

for t in test:
    print(t)
    print(b.merge(t))