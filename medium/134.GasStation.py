# There are n gas stations along a circular route, where the amount of
# gas at the ith station is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas
# to travel from the ith station to its next (i + 1)th station. You begin
# the journey with an empty tank at one of the gas stations.
#
# Given two integer arrays gas and cost, return the starting gas station's
# index if you can travel around the circuit once in the clockwise direction,
# otherwise return -1. If there exists a solution, it is guaranteed to be unique
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(cost)
        check = 0
        gasoline = 0

        for i in range(l):
            gasoline += gas[i]
            gasoline -= cost[i]
            if gasoline < 0:
                if i+1 < l:
                    check = i+1
                    gasoline = 0
                else:
                    check = -1
        if check > 0:
            for i in range(check):
                gasoline += gas[i]
                gasoline -= cost[i]
                if gasoline < 0:
                    check = -1
                    break
        return check
