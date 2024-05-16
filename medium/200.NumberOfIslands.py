# Given an m x n 2D binary grid grid which represents a map
# of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four
# edges of the grid are all surrounded by water.
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_isl = 0
        self.l = len(grid)
        self.c = len(grid[0])
        if not grid:
            return 0
        for i in range(self.l):
            for j in range(self.c):
                if grid[i][j] == "1":
                    n_isl += 1
                    self.explore(grid, i, j)

        return n_isl
    def explore(self, grid, i, j):
        if i < 0 or j < 0 or i >= self.l or j >= self.c:
            return
        if grid[i][j] == "1":
            grid[i][j] = "0"
            self.explore(grid, i+1, j)
            self.explore(grid, i, j + 1)
            self.explore(grid, i - 1, j)
            self.explore(grid, i, j - 1)
        else:
            return
