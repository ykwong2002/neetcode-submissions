class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        q = deque()

        rows, cols = len(grid), len(grid[0])

        # initialise queue of rotten fruits and number of fresh fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        def infect(r, c):
            nonlocal fresh
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or grid[r][c] == 2:
                return
            # rot the fresh fruit
            grid[r][c] = 2
            q.append((r, c)) # now it has to infect others also
            fresh -= 1

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft() # next rotten fruit to infect
                infect(r + 1, c)
                infect(r - 1, c)
                infect(r, c + 1)
                infect(r, c - 1)
            time += 1
        
        return time if fresh == 0 else -1
                

        
"""
Goal: return time taken for all fruits to become rotten, else -1
- multi-source BFS problem (closest rotten fruit will infect the fresh fruit)
- initialise number of fresh fruits
- initialise q with all rotten fruits
- initialise time as 0
- for the length of q (current number of rotten source fruits):
    - infect all nearby fresh fruits
"""