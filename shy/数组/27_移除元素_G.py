'''
Problem: 移除元素

Source: https://leetcode-cn.com/problems/remove-element/

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1: 给定 nums = [3,2,2,3], val = 3, 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。 你不需要考虑数组中超出新长度后面的元素。

示例 2: 给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
'''

class Solution:
    def removeElement(self, nums: list[int], val: int) ->int:
        # 双指针， uneqVal指向不等于val的元素，pointer指向当前元素
        uneqVal = 0 
        pointer = 0
        size = len(nums) # 数组长度, 可直接用len(nums)代替size

        while pointer < size:
            if nums[pointer] != val: # 当前元素不等于val时，将当前元素赋值给uneqVal指向的元素
                nums[uneqVal] = nums[pointer]
                uneqVal += 1 # 不等于val的元素+1
            pointer += 1 # 指针后移

        return uneqVal
    


