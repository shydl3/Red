'''
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，
且元素按顺时针顺序螺旋排列的正方形矩阵。
'''

class Solution:
    def solver(self, n: int):
        dirs = [(0,1), (1, 0), (0,-1), (-1,0)]
        matrix = [[0] * n for each in range(n)]

        row, col, dirIdx = 0, 0, 0
        for i in range(n*n):
            matrix[row][col] = i + 1

            dx, dy = dirs[dirIdx]
            r, c = row + dx, col + dy

            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                dirIdx = (dirIdx + 1) % 4
                dx, dy = dirs[dirIdx]

            row, col = row + dx, col + dy



