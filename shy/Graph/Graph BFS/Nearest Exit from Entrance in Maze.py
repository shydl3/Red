import collections

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        # 定义4个移动方向
        directions = ((1,0), (-1,0), (0,1), (0,-1))

        start_row, start_col = entrance
        maze[start_row][start_col] = "+"

        queue = collections.deque()
        queue.append([start_row, start_col, 0])

        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()

            # 向4个方向扩散，每扩散一层加入queue，distance + 1.
            # 起点entrance初始distance=0
            for dx, dy in directions:
                next_row, next_col = curr_row + dy, curr_col + dx

                # 判断下个位置的坐标有效则进一步执行。
                # 位于矩阵内、且不为墙，表示有效
                if 0<= next_row < rows and 0<= next_col < cols \
                and maze[next_row][next_col] == ".":
                    # 如果下一个坐标位置到达矩阵四个边缘之一，说明是一个有效出口，return
                    if next_row == 0 or next_row == rows - 1 \
                    or next_col == 0 or next_col == cols - 1:
                        return curr_distance + 1
                    # 将下一个位置设置为墙，防止重复访问
                    queue.append([next_row, next_col, curr_distance + 1])
                    maze[next_row][next_col] = "+"
        return -1