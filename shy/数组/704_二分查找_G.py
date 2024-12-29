'''
Problem: 704. 二分查找
Source: https://leetcode-cn.com/problems/binary-search/

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9     
输出: 4       
解释: 9 出现在 nums 中并且下标为 4     

示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2     
输出: -1        
解释: 2 不存在 nums 中因此返回 -1  
'''


class solution:
    def search(self, nums: list[int], target: int) -> int:
        # self表示类的实例本身 
        # 函数search接收两个参数，nums和target
        # list[int] 表示nums为int类型的列表
        # -> int 表示返回值为int类型
        left, right = 0, len(nums) - 1 # left下标为0， right下标为len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2 # 求中位数下标

            if nums[mid] == target: # 中位数等于目标值
                return mid
            elif nums[mid] < target: # 中位数小于目标值，取右半nums
                left = mid + 1
            else:  # 中位数大于目标值，取左半nums
                right = mid - 1

        return -1 # 不存在目标值，返回-1


