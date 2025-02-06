from heapq import *

heap = []

heappush(heap, 1)
heappush(heap, 2)

heap[0]

heappop(heap)

len(heap)

nums = [12, 98, 0, 200]
heap_new = heapify(nums)
