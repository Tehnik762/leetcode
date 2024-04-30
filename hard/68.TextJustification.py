# Given an array of strings words and a width maxWidth, format the text such that each
# line has exactly maxWidth characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack as many words as you
# can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible. If the number
# of spaces on a line does not divide evenly between words, the empty slots on the left
# will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left-justified, and no extra space is inserted between words.
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n_words = len(words)
        i = 1
        strings = []
        temp = words[0]
        while i < n_words:
            if len(temp) + len(words[i]) + 1 > maxWidth:
                strings.append(temp)
                temp = words[i]
            else:
                temp = temp+" "+words[i]
            i += 1
        strings.append(temp)
        j_str = []
        for s in strings[:-1]:
            l_string = len(s)
            rest = maxWidth - l_string
            if rest == 0:
                j_str.append(s)
            else:
                c_spaces = s.count(" ")
                if c_spaces < 1:
                    j_str.append(s.ljust(maxWidth))
                else:
                    words_in_a_string = s.split()
                    l_words = len(words_in_a_string)
                    l_spaces = l_words-1
                    rest += l_spaces
                    spaces = ["" for _ in range(l_spaces)]
                    step = 0
                    while rest > 0:
                        rest -= 1
                        spaces[step] += " "
                        if step == l_spaces-1:
                            step = 0
                        else:
                            step += 1
                    j_string = []
                    for j in range(l_spaces):
                        j_string.append(words_in_a_string[j])
                        j_string.append(spaces[j])
                    j_string.append(words_in_a_string[-1])
                    j_str.append("".join(j_string))
        j_str.append(strings[-1].ljust(maxWidth))
        return j_str

