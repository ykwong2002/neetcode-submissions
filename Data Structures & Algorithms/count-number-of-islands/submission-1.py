class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": # if land is found
                    count += 1
                    dfs(r, c) # convert all neighbouring lands to water to avoid recounting
        
        return count

"""
Goal: Find number of unique islands
- Use DFS
- Track number of islands
- Upon finding first land, increase island count and perform DFS on it
    - in DFS, convert all connected lands into water to prevent revisiting
    - recursively perform DFS on top, down, left, right
"""