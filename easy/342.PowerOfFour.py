# Given an integer n, return true if it is a power of four. Otherwise, return false.
#
# An integer n is a power of four, if there exists an integer x such that n == 4x.x

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 4:
            ost = n % 1
            if ost > 0:
                return False
            test = str(int(n))
            test = test[-1]
            if test == "4" or test == "6":
                n = n/4
            else:
                return False
        ost = n%1
        if ost > 0:
            return False
        n = int(n)
        if n == 4 or n == 1:
            return True
        else:
            return False
