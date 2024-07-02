# Given a string s, return the number of palindromic substrings in it.
#
# A string is a palindrome when it reads the same backward as forward.
#
# A substring is a contiguous sequence of characters within the string.

class Solution:
    def countSubstrings(self, s: str) -> int:
        new_s = "^!" + "!".join(s) + "!~"
        n = len(new_s)
        res = [0 for _ in range(n)]
        c = 0
        r = 0
        for i in range(1, n-1):
            mirror = 2*c - i
            if r > i:
                res[i] = min(r-i, res[mirror])

            while new_s[i + res[i] + 1] == new_s[i - res[i] - 1]:
                res[i] += 1

            if i +res[i] > r:
                c = i
                r = i + res[i]

        return sum((v + 1) // 2 for v in res)



test = [
["abc", 3],
["aaa", 6]
]

b = Solution()

for t in test:
    print(b.countSubstrings(t[0]) == t[1])