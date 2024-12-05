# You are given row x col grid representing a map where grid[i][j] = 1
# represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island
# (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected
# to the water around the island. One cell is a square with side length 1.
# The grid is rectangular, width and height don't exceed 100. Determine
# the perimeter of the island.
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        len_grid = len(grid)
        len_row = len(grid[0])
        top, left, bottom, right = 0, 0, len_grid - 1, len_row - 1
        for i in range(len_grid):
            for j in range(len_row):
                if grid[i][j] == 1:
                    if i == top:
                        perimeter += 1
                    if i == bottom:
                        perimeter += 1
                    if j == left:
                        perimeter += 1
                    if j == right:
                        perimeter += 1
                    if i > top:
                        if grid[i - 1][j] == 0:
                            perimeter += 1
                    if i < bottom:
                        if grid[i + 1][j] == 0:
                            perimeter += 1
                    if j > left:
                        if grid[i][j - 1] == 0:
                            perimeter += 1
                    if j < right:
                        if grid[i][j + 1] == 0:
                            perimeter += 1
        return perimeter

