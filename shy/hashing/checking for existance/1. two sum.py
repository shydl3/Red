'''
Given an array of integers nums and an integer target,
return index of two numbers such that they add up to target.
You cannot use the same index twice.

输出：
一个包含两个索引的列表 [i, j]，使得 nums[i] + nums[j] == target。
如果没有找到，返回 [-1, -1]。
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {} # 字典用于存储已经访问过的数值和它们的索引

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            # 如果complement已经存在于字典中，返回当前索引和补数的索引
            if complement in dic:
                return [i, dic[complement]]

            # 字典键值对顺序
            # element：index
            dic[num] = i

        return [-1, -1]

# since it wants the indices of the numbers, 
# we need to use a hashing map to "remember" what indices the numbers are at.