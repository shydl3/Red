from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        stack = [0]
        seen = {0}
        ans = 0

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        # while stack:
        #     node = stack.pop()
        #     for neighbor in graph[node]:

        # for node in range(n):
        #     for neighbor in graph[node]:
        #         if neighbor not in seen:
        #             ans += 1

        for node in range(n):
            if node not in seen:
                dfs(node)
                ans += 1
        return ans
