class Solution(object):
    def maxAreaOfIsland(self, grid: list[list[int]]):
        seen = set()
        def area(x, y):
            if not (
                0 <= x < len(grid)
                and 0 <= y < len(grid[0])
                and (x, y) not in seen
                and grid[x][y]
            ):
                return 0
            seen.add((x, y))
            return (
                1 + area(x+1, y) + area(x-1, y) + area(x, y-1) + area(x, y+1)
            )
        return max(area(x, y) for x in range(len(grid)) for y in range(len(grid[0])))

