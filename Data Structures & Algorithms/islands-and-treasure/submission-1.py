class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        # Initialise queue with treasure chests
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))
        
        def addRoom(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            q.append((r, c))
        
        # Perform BFS
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1

"""
Goal: fill each land cell with distance to nearest treasure chest
- only use in place modification
- multi-source BFS since we want nearest distance
- get rows and cols
- initialise a visited set to keep track of what i have visited and prevent overwriting shortest distance
- initialise a queue with all treasure chests
- while queue is not empty:
    - pop the cell out, change its distance
    - add its neighbors to the queue (if valid)
"""