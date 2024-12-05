# There are n children standing in a line. Each child is assigned a rating
# value given in the integer array ratings.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the
# candies to the children.
#
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        res = [1]*l
        for i in range(1, l):
            if ratings[i-1] < ratings[i]:
                res[i] += res[i-1]
            elif ratings[i-1] > ratings[i] and res[i-1] == res[i]:
                res[i-1] += 1

        for i in range(l-2, 0, -1):
            if res[i-1] == res[i+1] and ratings[i] > max(ratings[i+1], ratings[i-1]):
                res[i] = res[i+1]+1
            if ratings[i-1] == ratings[i+1] == ratings[i]:
                res[i] = 1
            if ratings[i+1] < ratings[i] and res[i] == res[i+1]:
                res[i] +=1
            if ratings[i-1] > ratings[i] and res[i-1] < res[i]:
                res[i-1] = res[i] + 1
        if l > 1:
            if ratings[0] > ratings[1] and res[0] <= res[1]:
                res[0] = res[1] + 1
        return sum(res)
