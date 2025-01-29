'''
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''

import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []  # 存放较大的一半元素
        self.max_heap = []  # 存放较小的一半元素

    # 调用时添加一个num
    def addNum(self, num: int) -> None:
        # 由于heapq默认生成最小堆，因此添加元素时取负值，即得到最大堆
        # 使用max_heap维持一个最大堆，num先添加到max_heap
        heapq.heappush(self.max_heap, -num)
        # 然后将max_heap堆顶元素弹出并取负值（即得到原值）并加入min_heap
        # 这样会确保min_heap始终得到max_heap的最大值，
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # 通过执行平衡，当minheap元素多于maxheap，向maxheap添加minheap的堆顶元素，即最小元素（并取负值，维持最大堆性质）
        # 这会使得minheap将存储所有元素最大一半那部分
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    '''
    若只调用一次addNum，（只传入一个元素），这个元素会先添加到maxheap，然后被弹出添加到minheap，
    然后触发len(self.min_heap) > len(self.max_heap)，又被添加到maxheap
    因此addNum执行完会确保len(self.min_heap) <= len(self.max_heap)
    要么maxheap元素多一个，要么两个堆数量相等
    '''

    # 调用时返回中位数
    def findMedian(self) -> float:
        # 如果maxheap元素更多，代表所有元素较小一半部分，和中位数都在maxheap中。（代表总元素个数奇数）
        # 而maxheap堆顶就是实际值最大的中位数
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        # 否则中位数需要取平均值
        return (self.min_heap[0] - self.max_heap[0]) / 2

