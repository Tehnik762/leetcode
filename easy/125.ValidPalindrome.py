# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanum = "zxcvbnmasdfghjklpoiuytrewq1234567890"
        l = len(s)
        if l == 1:
            return True
        point1 = 0
        point2 = l-1
        while True:
            while s[point1] not in alphanum and point1 < l-1:
                point1 += 1
            while s[point2] not in alphanum and point2 > 0:
                point2 -= 1
            if point1 == point2 or point2 < point1:
                break
            if s[point1] != s[point2]:
                return False
            point1 += 1
            point2 -= 1
        return True
