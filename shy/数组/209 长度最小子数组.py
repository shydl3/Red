'''
给定一个含有 n 个正整数的数组和一个正整数 s ，
找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。
如果不存在符合条件的子数组，返回 0。
'''
# 滑动窗口
class Solution:
    def minSubArray(self, s, nums):
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0

        while end < n:
            total += nums[end]
            while total > s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1

            end += 1

        return 0 if ans == n+1 else ans








