# Given two strings ransomNote and magazine, return true if ransomNote
# can be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_len = len(ransomNote)
        m_len = len(magazine)
        if r_len > m_len:
            return False
        magazine = list(magazine)
        ransomNote = list(ransomNote)
        for x in ransomNote:
            c = magazine.count(x)
            if c > 0:
                magazine.remove(x)
            else:
                return False
        return True

b = Solution()
print(b.canConstruct("aa", "ab"))