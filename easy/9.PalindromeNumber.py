# Given an integer x, return true if x is a
# palindrome, and false otherwise.
#

class Solution:
    def isPalindrome(self, x: int) -> bool:
        step = 10
        check = -1
        prev = 0
        res = ""
        if x < 0:
            return False
        while check != x:
            check = x%step
            step *= 10
            res += str(int((check-prev)/(step/100)))
            prev = check
        return int(res) == x

