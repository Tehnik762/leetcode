# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer
# range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#

class Solution:
    def reverse(self, x: int) -> int:
        stop = 2147483647
        if abs(x) > stop:
            return 0
        res = str(x)
        l = len(res)-1
        new =""
        otr = False
        for i in range(l, -1, -1):
            if res[i] == "-":
                otr = True
            else:
                new += res[i]
                if abs(int(new)) > stop:
                    return 0
        if otr == True:
            return -int(new)
        else:
            return int(new)
