class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maximum = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maximum = max(maximum, dfs(r, c))
        
        return maximum
"""
Goal: return maximum area of an island
- DFS
- keep track of maximum
- iterate through each cell
    - if find land, perform dfs and get the area of that island
        - 1 + top + down + left + right
        - convert all the land into water to prevent revisiting (can also add to visited set)
    - update maximum
"""