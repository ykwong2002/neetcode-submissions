class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set() # keep track of who has been updated / visited
        q = deque()

        # Initialise the queue with all treasure chests O(m x n)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        def addRoom(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            q.append((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                visited.add((r, c))
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1
"""
Goal: fill all land cells with distance to nearest treasure
- BFS since need to find nearest distance
- rows = len(grid), cols = len(grid[0])
- need a visited set to keep track of which cells have been visited to prevent overwriting
- need a queue to perform BFS
- dist = 0
- while q is non empty:
    - for the length of the queue, update the cell with the dist for this iteration
    - add top, down, left, right neighbors
"""