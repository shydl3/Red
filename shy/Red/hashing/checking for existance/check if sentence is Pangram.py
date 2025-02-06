'''
Pangram: 全字母句子是指英文字母表中每个字母都出现至少一次的句子。
Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.
'''

# set
class Solution:
    def checkIfPangra(self, sentence: str) -> bool:
        seen = set(sentence)

        return len(seen) == 26

