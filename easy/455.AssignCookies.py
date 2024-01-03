# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
#
# Each child i has a greed factor g[i], which is the minimum size of a cookie
# that the child will be content with; and each cookie j has a size s[j].
# If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        greed = 0
        size = 0
        res = 0
        len_greed = len(g)
        len_size = len(s)
        while greed < len_greed and size < len_size:
            if g[greed] <= s[size]:
                res += 1
                greed += 1
                size += 1
            else:
                greed += 1
        return res

