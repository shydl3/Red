'''
Given an array of integers nums and an integer limit,
return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 2:

Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
'''

from collections import deque


# 使用两个双端队列deque + 滑动窗口
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()

        left = 0
        max_length = 0

        # 更新滑动窗口右侧索引
        for right in range(len(nums)):
            # 若当前数值>max_deque末尾值（最近入队），弹出队列末尾值
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            # 直到当前数值最大，则入队。
            # 确保max_deque向右递减
            max_deque.append(nums[right])

            # 同理，确保min_deque向右递增排列
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length