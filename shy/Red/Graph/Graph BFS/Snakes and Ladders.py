from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        # 创建长度为 n^2 +1 的cells列表，用于存储棋盘上的编号与二维坐标的映射。
        # 后面的迭代对象是格子的label值。
        cells = [None] * (n ** 2 + 1)
        label = 1
        columns = list(range(0, n))

        # 从n-1行开始（最后一行），步长为-1，即每次往上循环一行
        for row in range(n - 1, -1, -1):
            # cells列表记录每个格子的值和row，col坐标对应关系
            for column in columns:
                cells[label] = (row, column)
                # label = 格子的值
                label += 1
            # 每行交替从左到右或从右到左
            columns.reverse()

        # 设置距离数组，到每个格子的最小距离。 -1表示未访问
        distance = [-1] * (n ** 2 + 1)
        queue = deque([1])
        distance[1] = 0

        while queue:
            # 当前格子（从label对应row，col）
            curr = queue.popleft()
            # 模拟骰子投掷的结果（1 到 6 步）
            for next in range(curr + 1, min(curr + 6, n ** 2) + 1):
                # 根据label对应到坐标
                row, column = cells[next]

                # 在蛇梯棋中，某些格子可能包含“蛇”或“梯子”，这些格子会将玩家强制跳转到另一个编号对应的格子位置（即目标编号）
                # 如果当前格子没有“蛇”或“梯子”，则玩家正常停留在当前编号。

                # 如果 board[row][column] != -1：说明格子有蛇或梯子，board[row][column] 就是跳转目的地的格子label值
                # 如果 ！= -1，保持在next（原本下一步要访问的）
                desti = (board[row][column] if board[row][column] != -1 else next)

                if distance[desti] == -1:
                    distance[desti] = distance[curr] + 1
                    queue.append(desti)

        # # 返回终点编号的步数
        return distance[n * n]
