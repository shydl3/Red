from collections import deque

class Solution:
    def openLock(self, deadends: list[int], target: str) -> int:

        # 遍历返回状态节点node（以string存储）所有的可能状态（邻居节点）
        # 四个轮盘，向前向后移动，2^4个邻居节点
        def neighbors(node: str) -> list[str]:
            ans = []
            for i in range(4):
                num = int(node[i])
                for change in [-1, 1]:
                    x = (num + change) % 10
                    # node[:i]前i个字符，不包括i
                    # node[i+1:]第i+1开始的所有字符
                    ans.append(node[:i] + str(x) + node[i+1:])

            return ans

        if "0000" in deadends:
            return -1

        #寻找最短路径，使用deque BFS
        queue = deque([("0000", 0)])
        seen = set(deadends)
        seen.add("0000")

        while queue:
            node, steps = queue.popleft()
            if node == target:
                return steps

            for neighbor in neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, steps+1))

        return -1



