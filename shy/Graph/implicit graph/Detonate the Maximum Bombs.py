from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        # defaultdict(list)：创建一个默认值为 list列表 的字典。
        # 因此graph：是一个字典，它的值默认是空列表 []。
        # 当 graph[1] 第一次被访问 时，它 不存在，但 defaultdict 自动创建 graph[1] = []（空列表）。
        graph = defaultdict(list)
        n = len(bombs)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                # 遍历并添加在其半径范围内的节点
                # graph[x] == [y] 且 graph[y] == [x] 代表无向边
                # 这里不一定是无向边，除非相互覆盖
                if ri**2 >= (xi - xj)**2 + (yi - yj)**2:
                    graph[i].append(j)

        def dfs(curr, visited):
            visited.add(curr)
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
            return len(visited)


        ans = 0
        # 对每个节点都执行dfs，并初始化空的visited，确保独立计算答案
        # 找到最长的dfs链
        for i in range(n):
            visited = set()
            ans = max(ans, dfs(i, visited))

        return ans


