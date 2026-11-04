class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initialise hashsets for each col, rol and square
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key is (r // 3, c // 3) --> scales it to the index of larger square

        for r in range(9):
            for c in range(9):
                # if empty cell, move to next iteration
                if board[r][c] == ".":
                    continue
                # if cell has value and value alr exists in row / col / square, return False
                if (board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                # if cell has value and value does NOT exist in row / col / square, append
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True