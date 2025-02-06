import heapq

class Solution:
    def maxNumberOfApples(self, weight: list[int]) -> int:
        # use min heap
        heapq.heapify(weight)
        ans = curr_units = 0

        while weight and curr_units + weight[0] <= 5000:
            curr_units += heapq.heappop(weight)
            ans += 1
        return ans
