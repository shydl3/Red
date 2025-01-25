'''
There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

Note that node 0 will not be a restricted node.
'''
import collections


class Solution:
    # BFS
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n
        for node in restricted:
            seen[node] = True

        ans = 0
        queue = collections.deque([0])
        seen[0] = True

        while queue:
            curr_node = queue.popleft()
            ans += 1
            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)

        return ans

    # dfs
    def sol2(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        neighbors = collections.defaultdict(list)
        for node_a, node_b in edges:
            neighbors[node_a].append(node_b)
            neighbors[node_b].append(node_a)

        seen = [False] * n
        for node in restricted:
            seen[node] = True

        def dfs(node: int):
            self.ans += 1
            seen[node] = True
            for next_node in neighbors[node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    dfs(next_node)


        self.ans = 0
        dfs(0)
        return self.ans
