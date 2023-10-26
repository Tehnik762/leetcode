# Given an integer n, return true if it is a power of two. Otherwise, return false.
#
# An integer n is a power of two, if there exists an integer x such that n == 2x.
#

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        b = str(bin(n)[2:])
        c = b.count("1")
        print(b)
        if c == 1:
            return True
        else:
            return False
