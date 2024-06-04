# The string "PAYPALISHIRING" is written in a zigzag pattern on a given
# number of rows like this: (you may want to display this pattern in a
# fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ["" for _ in range(numRows)]
        n = 0
        down = True
        for l in s:
            res[n] += l
            if n+1 == numRows:
                down = False
                n -= 1
            elif n == 0:
                down = True
                n += 1
            elif down:
                n += 1
            else:
                n -= 1
        return "".join(res)
