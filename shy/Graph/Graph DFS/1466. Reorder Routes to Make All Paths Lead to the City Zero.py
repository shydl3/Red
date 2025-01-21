'''
有 n 个城市（从 0 到 n−1 编号），它们通过 n−1 条有向道路连接，并且这 n−1 条道路构成了一棵有向树。
因为是树结构，忽略方向后，任意两座城市之间正好只有一条简单路径。

道路为单向，connections[i] = [ai, bi]表示方向为 ai -> bi
Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
例如 connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
反转某些道路，从而使得任意一个城市都可以到达 城市0
求最小的反转数量
'''
from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # roads记录节点联通情况, 按照x->y顺序记录
        roads = set()

        # 生成graph
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x, y))

        # 使用集合保存访问过的节点
        seen = {0}

        # 递归dfs，从起始节点遍历邻居节点
        # ans初始化在递归函数中，也就是每次递归独立计算传入节点的需要反转的边
        # 每次递归返回时会合并答案
        def dfs(node):
            ans = 0
            for neighbor in graph[node]:
                # 如果邻居节点第一次访问，且存在x->y方向道路（road是按照x->y顺序存储的）
                # 因为最初从 dfs(0) 开始递归，也就是说遇到向外发散的子节点 (x->y)，都需要反转
                # 才会使任意一个节点都可以到达0
                if neighbor not in seen:
                    if (node, neighbor) in roads:
                        ans += 1
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans

        return dfs(0)


    # iteration version
    def iteration(self, n: int, connections: list[list[int]]) -> int:
        roads = set()
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x, y))

        ans = 0
        stack = [0]
        seen = {0}

        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node, neighbor) in roads:
                        ans += 1
                    seen.add(neighbor)
                    stack.append(neighbor)

        return ans

'''
time complexity is O(n) since we visit each node only once, and do constant work.
total number of edges is n-1 
'''
