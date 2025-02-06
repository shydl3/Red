from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # 判断传入坐标是否有效：在矩阵内且==1
        # 因为探索对象是==1的点
        def valid(x, y):
            return 0<=x<m and 0<=y<n and mat[x][y] == 1

        # 初始化参数
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        seen = set()

        # 标记所有==0的点。steps用于标记从每个点向外扩张的层数（距离）
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col, 1))
                    seen.add((row, col))

        # 上下左右，四个扩张方向
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # 循环所有标记的 0点
        while queue:
            row, col, steps = queue.popleft()

            # 四个方向移动，
            for dx, dy in directions:
                next_row = row + dx
                next_col = col + dy
                # 每次遇到新的==1点，当前steps就是从最近0点扩张过来的步数
                if (next_row, next_col) not in seen and valid(next_row, next_col):
                    seen.add((next_row, next_col))
                    # 把符合条件的1点加入队列，遍历完所有点结束
                    queue.append((next_row, next_col, steps + 1))
                    mat[next_row][next_col] = steps

        return mat


