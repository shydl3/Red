'''
given a binary array nums, return the max length of a contiguous subarray
with an equal number of 0 or 1


Input: nums = [0,1,0]
Output: 2
[0, 1] (or [1, 0])
'''


'''
1 <= nums.length <= 105
nums[i] is either 0 or 1
'''
from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        prefix_sum = 0
        sum_map = {0: -1} # sum : index
        max_length = 0

        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1

            # 若当前位置的prefix sum出现在记录中，说明可以相减使prefix sum=0，达到目标子数组。
            # 因此更新较大的长度
            if prefix_sum in sum_map:
                max_length = max(max_length, i - sum_map[prefix_sum])
            # 若当前prefix sum没有记录，保存 prefix_sum : index 等待后续
            else:
                sum_map[prefix_sum] = i

        return max_length

input = [1,0,1,1,1,0,1,0,0,0]
solu = Solution()
print(solu.findMaxLength(nums = input))