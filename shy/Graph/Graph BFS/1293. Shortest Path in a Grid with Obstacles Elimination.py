from collections import deque

class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        def valid(x, y):
            return 0<=x<m and 0<=y<n

        # curr_x, curr_y, k-limit, steps
        queue = deque([(0, 0, k, 0)])
        # set the start location
        seen = {(0, 0, k)}
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue:
            curr_x, curr_y, k_remain, steps = queue.popleft()
            if curr_x == m-1 and curr_y == n-1:
                return steps

            for dx, dy in directions:
                next_x = curr_x + dy
                next_y = curr_y + dx
                # only move on when next location is valid and == 0 (no barrier)
                if valid(next_x, next_y):
                    if grid[next_x][next_y] == 0:
                        if (next_x, next_y, k_remain) not in seen:
                            # pass on k
                            seen.add((next_x, next_y, k_remain))
                            queue.append((next_x, next_y, k_remain, steps + 1))

                    elif k_remain and (next_x, next_y, k_remain - 1) not in seen:
                        seen.add((next_x, next_y, k_remain - 1))
                        queue.append((next_x, next_y, k_remain - 1, steps + 1))

        return -1

'''
have n*k 'states' in total. k is the given limit number, n is nodes
m is number of edges

work done at each state is O(1), constant
time complexity is O(m * n*k)
'''
