'''
Given an integer array nums and an integer k,
return the k most frequent elements. It is guaranteed that the answer is unique.
'''

from collections import Counter
import heapq

class solution:
    def topKFreqquent(self, nums: list[int], k: int) -> list[int]:
        # Counter 访问不存在的元素不会报错，而是返回 0。
        # collections.Counter用于对迭代元素计数
        counts = Counter(nums)
        heap = []

        # Counter形式： (迭代元素, 出现次数)
        for key, val in counts.items():
            # 在 Python heapq 中，默认按照元组的第一个元素进行排序。
            # 因此需要heappush(出现次数，迭代元素)， 才是正确的最小堆
            heapq.heappush(heap, (val, key))
            # 弹出堆顶最小元素，直到剩余k个best元素
            if len(heap) > k:
                heapq.heappop(heap)

        return [n[1] for n in heap]