# Given a string containing digits from 2-9 inclusive, return all
# possible letter combinations that the number could represent. Return the
# answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.letters
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        line = []
        l_digits = len(digits)
        if l_digits != 0:
            for i in range(l_digits-1, -1, -1):
                button = letters[int(digits[i])]
                temp = []
                for j in button:
                    temp.append(j)
                if i == l_digits - 1:
                    line = temp
                else:
                    cache = []
                    for j in line:
                        for k in temp:
                            cache.append(k + j)
                    line = cache
        return line
