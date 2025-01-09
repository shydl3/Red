'''
given an array of integers nums, and an integer k
return the total number of subarrays that sum equals to k

constraints:
1 <= nums.length <= 2*10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
'''

# 目标是计算数组中连续子数组的和等于 k 的个数。
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # 记录prefix sum出现的次数
        counts = defaultdict(int)

        counts[0] = 1
        ans = curr = 0

        for num in nums:
            # current prefix sum is curr
            curr += num

            # 当前索引位置若满足条件：curr − satisfying_prefix_sum = k  ⟹  satisfying_prefix_sum = curr−k
            # 检查是否存在满足条件的prefix sum
            # 如果不存在 [curr-k] 的键， defalutdic不会报错，默认返回0
            # 满足条件，则代表当前位置有 counts[satisfying_prefix_sum] 个满足条件的子数组
            # 迭代至数组最后一个元素，即是答案。
            ans += counts[curr -k]

            # 更新当前prefix sum记录
            counts[curr] += 1

        return ans