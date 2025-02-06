'''
Given a directed acyclic graph, (DAG 有向无环图)
with n vertices numbered from 0 to n-1,
and an array edges where edges[i] = [fromi, toi]  represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable.
It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

返回最少的节点数，从这些节点按路线顺序可以访问到所有节点（间接访问也算）
也就是无法从其他节点到达的最小节点集
找到所有节点的入度，并且只包括入度为零的节点。
因为只要入度大于零，就可以从其他节点访问到
'''

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        # n个节点，索引从0到 n-1
        indegree = [0] * n
        for x, y in edges:
            indegree[y] += 1

        return [node for node in range(n) if indegree[node] == 0]
