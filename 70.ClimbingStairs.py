# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            temp = 0
            curr = 1
            pre = 0

            for i in range(1, n+1):
                temp = curr
                curr += pre
                pre = temp
            return curr
