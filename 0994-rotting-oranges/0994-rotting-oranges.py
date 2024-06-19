from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        
        def isNeighborRotten(i, j, grid):
            for dx, dy in dirs:
                r, c = i + dx, j + dy
                if 0 <= r < m and 0 <= c < n and grid[r][c] == 2:
                    return True
            return False
        
        ans = 0
        
        while True:
            nextGrid = [[0] * n for _ in range(m)]
            # Calculate `nextGrid` based on `grid`.
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:  # fresh
                        # Any of the 4-directionally oranges is rotten
                        if isNeighborRotten(i, j, grid):
                            nextGrid[i][j] = 2
                        else:
                            nextGrid[i][j] = 1
                    elif grid[i][j] == 2:  # rotten
                        nextGrid[i][j] = 2  # Keep rotten.
            if nextGrid == grid:
                break
            grid = nextGrid
            ans += 1
        
        # Check if there are any fresh oranges left
        for row in grid:
            if 1 in row:
                return -1
        
        return ans
