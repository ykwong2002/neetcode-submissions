class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        q = deque()

        rows, cols = len(grid), len(grid[0])
        # Initialise fresh fruit count and add rotten fruits to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft() # pop out the next rotten fruit that will infect others

                for dr, dc in directions:
                    row, col = r + dr, c + dc # neighbours coordinates
                    if (row in range(len(grid))) and (col in range(len(grid[0]))) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1

"""
Goal: return total no. of minutes for all fresh fruit to become rotten
- keep track of time (increases with each iteration)
- keep track of no. of fresh fruits left
- use q to track the rotten fruits and perform BFS
- while still have fresh fruits and queue of rotten fruits is non-empty:
    - iterate through length of queue if fruit was fresh, now it is rotten
"""