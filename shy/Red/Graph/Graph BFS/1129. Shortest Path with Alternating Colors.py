from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        # 定义常量 RED 和 BLUE，用于表示红色边和蓝色边
        RED = 0
        BLUE = 1

        # 当访问 graph[RED][x] 时，如果键 x 不存在，defaultdict 会自动创建一个 list 作为默认值。
        # 图的最终结构:
        # graph = {
        #     RED: {x1: [y1, y2, ...], x2: [y3, y4, ...], ...},
        #     BlUE: {x1: [z1, z2, ...], x2: [z3, z4, ...], ...}
        # }
        graph = defaultdict(lambda: defaultdict(list))
        for x, y in redEdges:
            graph[RED][x].append(y)
        for x, y in blueEdges:
            graph[BLUE][x].append(y)

        ans = [float('inf')] * n
        # 初始化队列，包含从节点 0 出发的两种初始状态：
        # (节点编号, 边的颜色, 当前步数)
        queue = deque([(0, RED, 0), (0, BLUE, 0)])
        # 初始状态
        seen = {(0,RED), (0,BLUE)}

        while queue:
            node, color, steps = queue.popleft()
            ans[node] = min(ans[node], steps)

            for neighbor in graph[color][node]:
                if (neighbor, 1 - color) not in seen:
                    seen.add((neighbor, 1-color))
                    queue.append((neighbor, 1-color, steps+1))

        return [x if x != float('inf') else -1 for x in ans]
