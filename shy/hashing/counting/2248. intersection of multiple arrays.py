'''
given a 2D array nums, where nums[i] is a non-empty array of
distinct positive integers

return the list of integers that are present in each array of nums sorted ascending
'''
from collections import defaultdict

'''
Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]

Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], 
and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
'''

class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        counts = defaultdict(int)

        # 遍历每个数组，记录元素的出现次数
        # 遍历每个子数组的set，防止单个数组内的重复元素被多次计数
        for arr in nums:
            for x in set(arr):
                counts[x] += 1

        n = len(nums)
        ans = []
        for key in counts:
            # 如果元素出现次数等于数组数量，说明该元素出现在所有数组中
            # 因为上一步从set中计数没有重复
            if counts[key] == n:
                ans.append(key)

        return sorted(ans)


