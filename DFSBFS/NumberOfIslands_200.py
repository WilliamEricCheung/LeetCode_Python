from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        islands = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    islands += 1
                    self.dfs(grid, i, j)
        return islands

    def dfs(self, grid: List[List[str]], i: int, j: int):
        m = len(grid)
        n = len(grid[0])
        if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

