class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        
        return area
"""
Goal: return the maximum area of an island
- initialise maximum_area variable to keep track of highest area
- each time we find a land, we perform dfs on it and turn the neighbouring land into water to avoid recounting
- as we dfs, we increase current area count by 1
- update the max
"""