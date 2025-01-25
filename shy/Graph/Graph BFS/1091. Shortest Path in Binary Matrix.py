from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]], n: int) -> int:
        if grid[0][0] == 1:
            return -1

        def valid(x, y):
            return (0 <= x < n and 0 <= y < n and grid[x][y] == 0)

        n = len(grid)
        seen = {(0, 0)}
        queue = deque([(0, 0, 1)])   # row, col, steps
        directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]

        while queue:
            x, y, steps = queue.popleft()
            if (x, y) == (n-1, n-1):
                return steps

            for dx, dy in directions:
                next_x, next_y = x + dy, y + dx
                if valid(next_x, next_y) and (next_x, next_y) not in seen:
                    seen.add((next_x, next_y))
                    queu