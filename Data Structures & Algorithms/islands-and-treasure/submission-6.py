class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque() # contain those to be updated
        visited = set() # contains visited cells

        # initialise q with sources (treasure chest)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        def addRoom(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            q.append((r, c))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft() # next to 
                visited.add((r, c)) # visit the cell
                grid[r][c] = distance # update the distance
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            distance += 1


"""
Goal: fill all land cells with distance to nearest treasure chest
- since need NEAREST, use BFS
- multi-source BFS (land cells closer will be filled first)
- q (queue initialised with treasure chests)
- visited (set containing cells visited before)

- for each length of queue, they share the same distance
- popleft --> update distance
- neighbours
"""