import heapq

class Solution:
    def lastStoneWeight(self, stones: list[list[int]]) -> int:
        # heapq默认根据列表生成最小堆，即父节点<=子节点
        # 通过负值，间接实现最大堆。
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        # heapify返回的不是排序后的列表，而是符合局部有序的堆（二叉树结构），以列表存储
        # heapq.heappop() 弹出的是堆顶元素（根节点），而非一定是列表最右边
        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first != second:
                heapq.heappush(stones, -abs(first - second))

        return -stones[0] if stones else 0