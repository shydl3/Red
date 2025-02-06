import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


    def sort(self, nums: list[int], k: int) -> int:
        # reverse=True 表示 降序排序（从大到小）。
        nums.sort(reverse=True)
        return nums[k-1]