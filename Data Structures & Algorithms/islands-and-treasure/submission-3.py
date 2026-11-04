class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        # initialise q with all sources (treasure chests)
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
            # for all those currently in the queue, it is {{distance}} away from chest
            for i in range(len(q)):
                r, c = q.popleft()
                visited.add((r, c))
                grid[r][c] = distance # update the cell with the distance
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            distance += 1

"""
Goal: fill all land cells with the distance to CLOSEST treasure chest
- multi-source BFS
- queue --> deque --> initialise with all treasure chests
- visited set of cells
- distance initialised as 0
- popleft the queue
    - if visited before, skip
    - fill it with the distance
    - add its land neighbors to the queue


"""