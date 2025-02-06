from collections import deque

class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        queue = deque([start])
        # 应该使用 set() 或者 set 语法 {value1, value2, ...}
        # {} 在 Python 里默认是一个空字典
        visited = set()

        while queue:
            node_idx = queue.popleft()
            if arr[node_idx] == 0:
                return True

            if node_idx in visited:
                continue

            visited.add(node_idx)

            # 遍历包含两个next jump index的 列表 ：
            for i in [node_idx - arr[node_idx], node_idx + arr[node_idx]]:
                if 0 <= i < n:
                    queue.append(i)


        return False

