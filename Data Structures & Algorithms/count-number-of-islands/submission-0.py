class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        rows, cols = len(grid), len(grid[0]) # no. of rows and cols

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            # else if it is a connected island, convert it to water
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": # if we found an island
                    count += 1
                    dfs(r, c) # convert all its neighbours to 0s to avoid double counting same island
        
        return count
"""
Goal: Find number of islands (total number of unique connected 1s)
- graph problem
- initialise global count of islands to 0
- perform DFS on any occurence of 1
    - increase count by 1
    - convert all its connected 1s to 0 so i dont count them again
"""