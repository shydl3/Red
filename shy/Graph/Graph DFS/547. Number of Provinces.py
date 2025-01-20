'''
There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.


Return the total number of provinces.

# 联通分量也就是一部分子图，联通分量之间不互通
'''

from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:

        # dfs函数
        # 递归遍历传入节点的所有邻居节点，将与当前节点直接或间接相连的所有节点标记为已访问
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        # 递归版dfs
        def dfs2(start):
            stack = [start]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)


        # build the graph
        # 根据 isConnected 矩阵，将图的连接关系存储在一个 defaultdict(list) 中
        # 创建一个defaultdict(list)，储存list，生成邻接表
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            # 只遍历矩阵的上三角部分，避免重复处理
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        seen = set()
        ans = 0

        # 每次循环内，依次对每个节点调用dfs函数，将与其联通的节点都加入seen
        # 因此下一个节点若没有出现在seen里，说明和前面的节点都不联通
        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)

        return ans

'''
the time complexity for DFS on graphs is usually O(n+e), 
where n is the number of nodes and e is the number of edges. 

In the worst-case scenario where every node is connected with every other node, e= n^2

Technically in this problem, the time complexity is O(n^2) 
because the input is given as an adjacency matrix, so we always need O(n^2) to build the hash map. 
'''

