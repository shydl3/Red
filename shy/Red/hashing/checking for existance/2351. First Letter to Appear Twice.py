# using hashing table or set to determine if an element exists is O(1)
# while an array takes O(n) to do this
# so probably reducing the runtime from O(n2) to O(n)

'''
given a string s, return the first character that
appears 2 times
the input is guaranteed to have duplicated characters
'''

# Bruteforce, O(n2) for nested loop
class Solution1:
    def repeatedCharacter(self, s: str) -> str:
        for i in range(len(s)):
            c = s[i]

            for j in range(i):
                if s[j] == c:
                    return c

        return ""


# using set, also a type of hashing table.
# now has O(n)
class Solution2:
    def repeatedCharacter(self, s) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)

        return ""


'''
example 3:
given an integer array nums, 
find all unique numbers x in nums that
x+1 not in nums AND x-1 not in nums
'''
def find_numbers(nums: list[int]):
    ans = []
    nums = set(nums)

    for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            ans.append(num)

    return ans





