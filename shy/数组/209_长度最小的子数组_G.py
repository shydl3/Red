'''
Problem: 长度最小的子数组
Source: https://leetcode-cn.com/problems/minimum-size-subarray-sum/

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
提示：

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
'''

class Solution:
    def minSubArrayLen(self, s:int, nums:list[int]) -> int:
        left, right, minLen, size = 0, 0, float('inf'), len(nums) # 初始化左右指针，最小数组长度初始化，数组长度
        sum = 0

        while right < size: # 右指针小于数组长度
            sum += nums[right]

            while sum >= s: # 当和大于等于s时，更新最小数组长度
                minLen = min(minLen, right - left + 1) # 更新最小组长度
                sum -= nums[left]
                left += 1

            right += 1

        return minLen if minLen != float('inf') else 0 # 如果minLen没有被更新过，说明没有符合条件的子数组，返回0





