'''
You are given an array of integers nums,
there is a sliding window of size k which is moving from the very left of the array to the very right.

You can only see the k numbers in the window.
Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # dq 是一个双端队列，用于存储当前窗口中可能成为最大值的元素索引。
        dq = deque()
        # res 是结果数组，用于存储每个滑动窗口的最大值
        res = []

        # k是固定的，代表窗口长度
        # 初始化第一个窗口（前k个元素）
        for i in range(k):
            # for deque, left is front, right is rear
            # dq[0]访问双端队列中的第一个元素（队首元素）。
            # dq[-1] 队列中的末尾元素

            # 若当前元素 > 上一个入队元素(队尾)：
            while dq and nums[i] >= nums[dq[-1]]:
                # deque.pop()弹出末尾（最右边）元素。因为它不可能成为当前或未来窗口的最大值。
                dq.pop()
            # 直到没有比当前更小的则添加当前索引，确保队列中索引对应的值向右递减
            # deque.append()会将当前索引添加到末尾，即deque[-1]
            dq.append(i)

        # 上面的for循环确保dq递减
        # 因此记录初始窗口的最大值
        res.append(nums[dq[0]])

        # 开始更新窗口
        for i in range(k, len(nums)):
            # 如果 dq[0] == i - k，说明队首索引超出了当前窗口范围，需要移除。
            if dq and dq[0] == i-k:
                dq.popleft()

            # 同理。如果当前值 nums[i] 大于或等于队尾对应的值，则弹出队尾索引。
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

            # 每次循环都更新一步窗口和对应的最大值。
            res.append(nums[dq[0]])

        return res