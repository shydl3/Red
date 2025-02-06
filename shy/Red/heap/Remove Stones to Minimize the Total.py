'''
piles[i] represents the number of stones in the ith pile

执行k次：任选一个pile[i], 并将其减半（floor(piles[i] / 2)）
可以选择相同的pile[i]多次

Return the minimum possible total number of stones remaining after applying the k operations.
'''

import heapq

class Solution:
    def minStoneSum(self, plies: list[int], k: int) -> int:
        heap = [-num for num in plies]
        heapq.heapify(heap)

        for _ in range(k):
            curr = heapq.heappop(heap)
            remove = curr // 2
            heapq.heappush(heap, -(curr - remove))

        return -sum(heap)
