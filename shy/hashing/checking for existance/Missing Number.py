'''
Missing Number
given an array nums containing n distinct numbers in the range [0, n]
return the only number that missing from the array
'''


# hashset
class Solution:
    def missingNumber(self, nums: list[int]):
        num_set = set(nums)

        n = len(nums) + 1

        for number in range(n):
            if number not in num_set:
                return number




