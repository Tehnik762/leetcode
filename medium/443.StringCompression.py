# Given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating
# characters in chars:
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead,
# be stored in the input character array chars. Note that group lengths that are
# 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
#
# You must write an algorithm that uses only constant extra space.
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        start = 0
        step = 0
        end = len(chars) - 1
        while step <= end:
            end = len(chars) - 1
            count = 1
            step += 1
            while start < end and chars[step] == chars[start]:
                count += 1
                if step >= end:
                    #count += 1
                    break
                step += 1
            for i in range (1, count):
                if start+i >= end:
                    chars.pop()
                    break
                else:
                    chars.pop(start+1)
            if count > 1:
                count = str(count)
                pos = 1
                for number in count:
                    chars.insert(start+pos, number)
                    pos += 1
                start += pos
            else:
                start += 1
            if step >= end:
                break
            step = start
        return len(chars)
