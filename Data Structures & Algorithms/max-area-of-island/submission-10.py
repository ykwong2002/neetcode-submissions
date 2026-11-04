class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            # convert this land to water
            grid[r][c] = 0
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # if land, update maximum
                    max_area = max(max_area, dfs(r, c))
        
        return max_area

"""
Goal: return maximum area of an island in the grid
- graph problem --> DFS
- iterate through all cells in the grid:
    - if see a land --> perform DFS on it
    - maximum = max(maximum and dfs(cell))
- in DFS: convert all connected land (same island) to water to prevent revisiting and recounting
- 
"""