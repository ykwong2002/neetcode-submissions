class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check the rows
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                elif board[row][i] in seen:
                    return False
                else:
                    seen.add(board[row][i])
        # Check the cols
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                elif board[i][col] in seen:
                    return False
                else:
                    seen.add(board[i][col])
        # Check the squares
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
                    else:
                        seen.add(board[row][col])
        
        return True
"""
Goal: Check if there are duplicates in each row, col or square
- use set to check since its O(1) lookup
- for square, to calculate row, row = (square//3) * 3 + i, where i is in range(3)
- for square, to calculate col, col = (square%3) * 3 + j, where j is in range(3)
"""