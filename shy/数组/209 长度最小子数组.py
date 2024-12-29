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








