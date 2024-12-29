'''
Problem: 977. 有序数组的平方
Source: https://leetcode-cn.com/problems/squares-of-a-sorted-array/

给你一个按非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1：

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]
示例 2：

输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
'''

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]: # list[int] 表示输入的是一个整数数组，返回的也是一个整数数组
        res = [0] * len(nums) # 初始化一个长度为nums的数组，用于存放结果
        left, right, index = 0, len(nums) - 1, len(nums) - 1   # index指针从后往前遍历

        while left <= right: 
            if nums[left] ** 2 > nums[right] ** 2:
                res[index] = nums[left] ** 2 # 从两端向中间遍历
                left += 1
            else:
                res[index] = nums[right] ** 2
                right -= 1
            index -= 1 # index指针从后往前遍历
        
        return res