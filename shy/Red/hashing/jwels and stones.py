'''
given strigns jewels representing types of stones that are jewels
and stones representing the stones you have

each character in stones is a type of stone you have
You want to know how many of the stones you have are also jewels
Letters are case sensitive, so "a" is considered a different type of stone from "A"

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

constraints:
1 <= jewels.length, stones.length <= 50
jewels and stones consists of only English letters
All the characters of jewels are unique
'''

class Solution:
    def numOfJewels(self, jewels: str, stones: str) -> int:
        Jset = set(jewels)
        return sum(s in Jset for s in stones)