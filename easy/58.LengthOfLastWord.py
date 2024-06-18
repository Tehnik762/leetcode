# Given a string s consisting of words and spaces, return the
# length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = s.split(" ")
        t = -1
        l_st= len(st)
        if l_st == 1:
            s = s.strip()
            return len(s)
        while t+l_st != 0:
            test = st[t]
            res = len(test)
            if res > 0:
                return res
            else:
                t -= 1
        return len(st[0])


test = [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
    ("a", 1),
    ("a ", 1),
]

b = Solution()

for t in test:
    print(b.lengthOfLastWord(t[0]) == t[1])
