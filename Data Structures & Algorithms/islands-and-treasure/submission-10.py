class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()

        # initialise queue with treasure chests
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        def process(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == -1 or (r, c) in visited:
                return
            visited.add((r, c))
            q.append((r, c))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                visited.add((r, c))
                grid[r][c] = distance
                # process the neighbors
                process(r + 1, c)
                process(r - 1, c)
                process(r, c + 1)
                process(r, c - 1)
            distance += 1
"""
Goal: modify grid in-place to fill land cells with closest distance to treasure chest
- multi-source BFS --> since need nearest
    - start radiating from all sources (treasure chest)
    - each wave of radiation is one distance
    - if visited, skip since shortest distance has been filled
- get rows and cols
- q to track cells to process (start with all treasure chests)
- visited set to track all visited cells (to avoid overwriting)
- go through all cells in the queue:
    - for length of current queue (same distance away)
        - popleft the queue
        - add to visited
        - fill with distance
        - process neighbors

- process:
    - if cell out of range or cell is water or cell in visited
        - return
    - else, its a valid land cell to continue radiating
    - add to visited, add to queue
    
"""