'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target
搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
'''

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


# time: O(logn)







