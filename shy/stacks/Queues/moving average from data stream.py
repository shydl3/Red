'''
given a stream of integers and a window size,
calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:
MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
'''

'''
Example 1:
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
'''

'''
Constraints:

1 <= size <= 1000
-105 <= val <= 105
At most 104 calls will be made to next.
'''

class MovingAverage1:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)

        # 从列表 queue 中提取最后 size （含起点）个元素（如果 size 大于列表长度，则提取整个列表）
        window_sum = sum(queue[-size:])
        # 计算正确的均值
        return window_sum / min(len(queue), size)
# 切片&求和 时间复杂度： O(k)， k=min(len(queue), size)

# 2. double-ended deque
from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()

        # number of elements seen so far
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1

        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, self.count)