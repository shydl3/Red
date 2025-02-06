'''
k projects allowed to be done
have w capital initially

capital[i]: ith project needs capital
profits[i] adds to capital when finish
'''

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # n projects in total
        n = len(profits)

        # 这里 zip() 将 capital 和 profits 对应元素组合成元组。
        # capital = [0, 1, 2]
        # profits = [5, 10, 15]
        # projects = [(0, 5), (1, 10), (2, 15)]

        projects = sorted(zip(capital, profits))
        heap = []
        i = 0

        # 在限制的完成k个任务范围内遍历，
        for _ in range(k):

            # the capital needed for ith sorted project
            # 将所需capital <= 当前capital的任务profit加入最大堆
            # 堆顶代表完成当前第x个任务时，所有可以做的任务的最大回报
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1

            # 如果堆是空的说明无法继续。return answer
            if len(heap) == 0:
                return w

            # 将当前（第x步）最大回报累加
            w += -heapq.heappop(heap)

        return w