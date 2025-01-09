'''
given an n*n matrix grid, return the number of pairs (R, C)
where R is a row and C is a column,
and R, Care equal if we consider them as 1D arrays


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

constrains:
n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 10^5
'''

from collections import defaultdict

# 用两个hash map （defaultdict） 储存每种排列计数的 row和col
# 先将数组转换为tuple，才能作为defaultdict字典的键
# 相同排列的数量相乘 row*col，累加，就是答案
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:

        def convert_to_key(arr):
            return tuple(arr)

        dic = defaultdict(int)
        for row in grid:
            dic[convert_to_key(row)] += 1

        dic2 = defaultdict(int)

        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])

            dic2[convert_to_key(current_col)] += 1

        ans = 0
        for arr in dic:
            ans += dic[arr] * dic2[arr]
        return ans