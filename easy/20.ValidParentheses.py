# Given a string s containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        pts = ["()", "{}", "[]"]
        while True:
            flag = 0
            for i in pts:
                search = s.find(i)
                if search > -1:
                    s = s.replace(i, "")
                    flag = 1
            if flag == 0:
                break
        if len(s) == 0:
            return True
        else:
            return False


