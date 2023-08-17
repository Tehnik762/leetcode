# Given an array of integers citations where citations[i] is the number
# of citations a researcher received for their ith paper, return the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: The h-index is
# defined as the maximum value of h such that the given researcher has published at
# least h papers that have each been cited at least h times.
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations = list(reversed(citations))
        for i in range(len(citations)):
            n = i+1
            if n > citations[i]:
                return i
        return len(citations)


