# You are given a string s and an array of strings words. All the strings
# of words are of the same length.
#
# A concatenated string is a string that exactly contains all the strings
# of any permutation of words concatenated.
#
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef",
# "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef"
# is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings
# in s. You can return the answer in any order.
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        test_words_dic = {}
        for w in words:
            if w in test_words_dic.keys():
                test_words_dic[w] += 1
            else:
                test_words_dic[w] = 1
        step = len(words[0])
        left = 0
        right = step
        stop_sign = len(s) - step
        res = []
        while left <= stop_sign:
            test_dic = test_words_dic.copy()
            check = left
            for i in range(len(words)):
                piece = s[left:right]
                if piece in test_dic.keys():
                    left += step
                    right += step
                    test_dic[piece] -= 1
                else:
                    break
            if max(test_dic.values()) == 0:
                res.append(check)
            left = check + 1
            right = left + step
        return res
