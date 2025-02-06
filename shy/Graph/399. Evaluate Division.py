from collections import defaultdict

class Solution:
    def solu(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:

        def answerQuery(start, end):
            if start not in graph:
                return -1

            seen = {start}
            stack = [(start, 1)]


            while stack:
                node, ratio = stack.pop()
                if node == end:
                    return ratio

                # graph 是一个 嵌套字典（邻接表表示法），用于存储带权重的有向图。
                # graph[node] 返回的是一个字典，其中 key 是邻居节点，value 是 node 到该邻居的权重
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor, ratio * graph[node][neighbor]))

            return -1

        # defaultdict(list) 是 Python 中 collections 模块提供的 默认字典（Default Dictionary），
        # 它的行为与普通字典类似，但在访问不存在的键时，会自动创建默认值（这里是 list）。

        # 使用嵌套字典（邻接表表示法）实现权重有向图
        # equations = [["a", "b"], ["b", "c"]]
        # values = [2.0, 3.0]
        # graph形式为 {'a': {'b': 2.0}, 'b': {'a': 0.5, 'c': 3.0}, 'c': {'b': 0.3333}}

        graph = defaultdict(dict)
        for i in range(len(equations)):
            upper, lower = equations[i]
            val = values[i]
            graph[upper][lower] = val
            graph[lower][upper] = 1/val

        ans = []
        for upper, lower in queries:
            ans.append(answerQuery(upper, lower))

        return ans










