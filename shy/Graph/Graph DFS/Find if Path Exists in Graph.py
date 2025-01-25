'''
There is a bi-directional graph with n vertices where each vertex is labeled from 0 to n - 1 (inclusive).

The edges in the graph are represented as a 2D integer array edges
where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
边都是双向，每两个节点之间至多一条边
没有指向自己的边

Given edges and the integers n, source, and destination,
return true if there is a valid path from source to destination, or false otherwise.
'''
from collections import defaultdict
from collections import deque

# 先生成 graph, 再迭代判断邻居节点
# DFS, 通常递归。也可以stack模拟递归
class Solution_DFS:
    def recursive_dfs(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = [False] * n

        # 递归函数会对当前节点进行判断
        # 因此不需要设置 seen[source] = True
        # 因为
        def dfs(curr_node) -> bool:
            if curr_node == destination:
                return True

            if not seen[curr_node]:
                seen[curr_node] = True
                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True
            return False

        return dfs(source)


    def iteration_dfs(self, n: int, edges: list[list[int]], source: int, destination: int):
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        stack = [source]
        seen = [False] * n
        seen[source] = True

        while stack:
            curr_node = stack.pop()
            for next_node in graph[curr_node]:
                if next_node == destination:
                    return True
                if not seen[next_node]:
                    seen[next_node] = True
                    stack.append(next_node)

        return seen[destination]


# bfs版本。使用双端队列collections.deque
class Solution_BFS:
    def recursive_dfs(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = [False] * n
        seen[source] = True
        queue = deque([source])

        while queue:
            curr_node = queue.popleft()
            if curr_node == destination:
                return True

            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)

            # 如果queue循环没有return True，说明没有符合条件
        return False