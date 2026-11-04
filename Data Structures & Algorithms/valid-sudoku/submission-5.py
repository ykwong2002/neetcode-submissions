class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9): # Iterate over each row
            seen = set()
            for i in range(9): # Iterate over each element in row
                if board[row][i] == ".":
                    continue
                elif board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9): # Iterate over each col
            seen = set()
            for i in range(9): # Iterate over each element in col
                if board[i][col] == ".":
                    continue
                elif board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True

"""
Goal: Check if all rows, cols and square have unique set of 1-9
- board is list of lists: board[r][c]

- Check all rows have no duplicates
    - compare set(row)
- Check all cols have no duplicates
    - compare set (col)
- Check all squares have no duplicates
[
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
]
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
(2, 0)
(2, 1)
(2, 2)
"""