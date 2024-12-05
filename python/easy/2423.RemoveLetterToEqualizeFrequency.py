# You are given a 0-indexed string word, consisting of lowercase English
# letters. You need to select one index and remove the letter at that index
# from word so that the frequency of every letter present in word is equal.
#
# Return true if it is possible to remove one letter so that the frequency
# of all letters in word are equal, and false otherwise.
#
# Note:
#
# The frequency of a letter x is the number of times it occurs in the string.
# You must remove exactly one letter and cannot choose to do nothing.


class Solution:
    def equalFrequency(self, word: str) -> bool:
        temp = {}
        for letter in word:
            if letter in temp.keys():
                temp[letter] += 1
            else:
                temp[letter] = 1
        temp_s = set(temp.values())
        l_temp_s = len(temp_s)
        if l_temp_s > 2:
            return False
        val = list(temp.values())
        l_val = len(val)
        if l_temp_s == 1:
            if l_val == 1:
                return True
        ones = 0
        if 1 in val:
            ones = val.count(1)
        if ones > 1:
            if ones == l_val:
                return True
        if ones == 1:
            return True
        max_val = max(val)
        min_val = min(val)
        if max_val - min_val == 1 and val.count(max_val) == 1:
            return True
        else:
            return False

