'''
给你一个按 非递减顺序 排序的整数数组 nums，
返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
'''

class Solution:
    def sortSquares(self, nums):
        n = len(nums)
        neg_index = -1

        for i, num in enumerate(nums):
            if num < 0:
                neg_index = i
            else:
                break

        ans = list()
        i, j = neg_index, neg_index + 1
        while i >= 0 or j < n:
            if i < 0:
                ans.append(nums[j] * nums[j])
                j += 1
            elif j == n:
                ans.append(nums[i] * nums[i])
                i -= 1
            elif nums[i] * nums[i] < nums[j] * nums[j]:
                ans.append(nums[i] * nums[i])
                i -= 1
            else:
                ans.append(nums[j] * nums[j])
                j += 1
        return ans



class Solution2:
    def sortedSquares(self, nums):
        return sorted(num * num for num in nums)





