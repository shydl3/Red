'''
given an integer array nums,
return the largest integer that only occurs once
if no integer occurs once, return -1
'''


class Solution:
    def func(self, nums: list[int]):
        occur_count = {}

        for num in nums:
            occur_count[num] = occur_count.get(num, 0) + 1

        filter = []
        for num, occur in occur_count.items():
            if occur == 1:
                filter.append(num)

        if len(filter) == 0:
            return -1
        else:
            return max(filter)