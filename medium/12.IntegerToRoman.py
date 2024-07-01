# Seven different symbols represent Roman numerals with the following values:
#
# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:
#
# If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
# If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
# Given an integer, convert it to a Roman numeral.
#


class Solution:
    def intToRoman(self, num: int) -> str:
        num_str = str(num)
        num_str = num_str[::-1]
        res = ""
        i = 0
        haystack = {
            "1": "I",
            "4": "VI",
            "5": "V",
            "9": "XI",
            "10": "X",
            "40": "LX",
            "50": "L",
            "90": "CX",
            "100": "C",
            "400": "DC",
            "500": "D",
            "900": "MC",
            "1000": "M"
        }


        for step in num_str:
            if step == "0":
                i += 1
                continue
            half = int(step)/2 >= 3
            cur = step + "".join(["0" for _ in range(i)])
            if cur in haystack.keys():
                res += haystack[cur]
            else:
                curr = "1" + "".join(["0" for _ in range(i)])
                if not half:
                    res += int(step)*haystack[curr]
                else:
                    gr = int(cur) - (int(step) - 5)*10**i
                    gr_step = int(step) - 5
                    res += gr_step*haystack[curr]  + haystack[str(gr)]
            i += 1
        return res[::-1]
