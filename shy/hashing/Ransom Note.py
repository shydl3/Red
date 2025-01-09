'''
given two strings ransomNote and magazine,
return True if ransomNote can be constructed by using letters from magazine, otherwise False

Each letter in magazine can only be used once in ransomNote.

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

from collections import defaultdict

class Solution:
    def sol(self, ransomNote: str, magazine: str) -> bool:
        dic1 = defaultdict(int)
        for letter in magazine:
            dic1[letter] += 1

        dic2 = defaultdict(int)
        for letter in ransomNote:
            dic2[letter] += 1

        for key in dic2:
            if dic2[key] > dic1[key]:
                return False
        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c not in magazine:
                return False

            location = magazine.index(c)
            magazine = magazine[:location] + magazine[location+1:]
        return True