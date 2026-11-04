class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0 # no. of fresh fruits
        q = deque() # stores rotten fruits
        time = 0

        # initialise fresh and q
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        def rot(r, c):
            nonlocal fresh
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or grid[r][c] == 2:
                return
            # if it was a fresh fruit, now it is not. add to queue of rotten fruits
            grid[r][c] = 2
            fresh -= 1
            q.append((r, c))

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft() # next rotten fruit
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)
            time += 1
        
        return time if fresh == 0 else -1
"""
Goal: return min number of minutes until 0 fresh fruits. if still got fresh fruits at the end --> -1
- multi-source BFS
- at each iteration, time += 1
- q (queue to store rotten fruits)
- fresh fruit count (to store number of fresh fruits for breaking condition)

- initialise q with rotten fruits, fresh with fresh fruits count
- pop q to get rotten fruit, bfs to rot surrounding fruits
"""