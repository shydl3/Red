'''
Problem: 59. Spiral Matrix II
Source: https://leetcode-cn.com/problems/spiral-matrix-ii/

给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]
'''

class Solution:
    def generateMatrix(self, n:int) ->list[list[int]]:
        Res = [[0] * n for _ in range (n)] # 列表推导式生成n*n的矩阵
        startX, startY = 0, 0
        loop, mid = n // 2, n // 2 # 迭代次数、矩阵中心点
        num = 1

        for offset in range(1, loop + 1): # 每循环一层偏移量加1，偏移量从1开始。loop + 1 的作用是让 offset 的范围包括 loop，即从 1 到 loop
            for j in range(startY, n - offset): # 从左至右，左闭右开
                Res[startX][j] = num # 行不变，列变
                num += 1 
            for i in range(startX, n - offset):
                Res[i][n - offset] = num
                num += 1
            for j in range(n - offset, startY, -1):
                Res[n - offset][j] = num
                num += 1
            for i in range(n - offset, startX, -1):
                Res[i][startY] = num
                num += 1
            startX += 1 # 行列坐标向内收缩
            startY += 1 # 行列坐标向内收缩

        if n % 2 != 0:
            Res[mid][mid] = num # n 为奇数时，最中间的位置
        
        return Res


