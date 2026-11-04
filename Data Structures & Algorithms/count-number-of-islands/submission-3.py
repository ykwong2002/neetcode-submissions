class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == "0":
                return
            # convert this land into water
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        
        return count

"""
Goal: return number of islands (connected lands)
- get no. of rows and cols
- go through each cell:
    - if land:
    - increment count
    - dfs to convert all connected land to water to avoid recounting
"""