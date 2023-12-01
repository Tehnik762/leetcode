# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in
# s will be separated by at least one space.
#
# Return a string of the words in reverse order concatenated by a single space.
#
# Note that s may contain leading or trailing spaces or multiple spaces between
# two words. The returned string should only have a single space separating the words.
# Do not include any extra spaces.


class Solution:
    def reverseWords(self, s: str) -> str:
        stor = []
        word = ""
        for letter in s:
            if letter != " ":
                word += letter
            else:
                if word != "":
                    stor.insert(0, word)
                    word = ""
        if word != "":
            if len(stor) > 0:
                res = word + " "
            else:
                return word
        else:
            res = ""
        for word in stor:
            res += word + " "
        return res[:-1]

