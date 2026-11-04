class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set() # cells that can rch pac and atl respectively

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(cols):
            # first row --> pacific ocean
            dfs(0, c, pac, heights[0][c])
            # last row --> atlantic ocean
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        for r in range(rows):
            # first col --> pacific ocean
            dfs(r, 0, pac, heights[r][0])
            # last col --> atlantic ocean
            dfs(r, cols - 1, atl, heights[r][c])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res