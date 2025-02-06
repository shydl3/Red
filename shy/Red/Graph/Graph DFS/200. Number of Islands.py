'''
Given an m x n 2D binary grid grid,
which represents a map of '1's (land) and '0's (water), return the number of islands.

return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
'''
from threading import get_ident

from pkg_resources import null_ns_handler


class Solution:
    def numIslands(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        # 矩阵每个元素都循环
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果当前元素=="1"，调用dfs查找与其相邻的"1"并清零后，可以累加答案
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num_islands += 1

        return num_islands

    def dfs(self, grid, x, y):
        if (
            # 如果x, y坐标超出矩阵范围，
            # 或者grid[x][y]不是"1" (非陆地)
            # 则不执行操作
            x<0
            or y<0
            or x >= len(grid)
            or y >= len(grid[0])
            or grid[x][y] != "1"
        ):
            return
        # 否则将grid[x][y] 变为“0” （原值不是0）
        # 代表与传入的初始坐标相连的都被清除，方便后续处理
        grid[x][y] = "0"

        # 并朝上下左右四个方向递归调用相同步骤
        self.dfs(grid, x - 1, y)
        self.dfs(grid, x + 1, y)
        self.dfs(grid, x, y - 1)
        self.dfs(grid, x, y + 1)

'''
Time complexity : O(M×N) 
where M is the number of rows and N is the number of columns.

Space complexity : worst case O(M×N) in case that the grid map
is filled with lands where DFS goes by M×N deep.
'''
