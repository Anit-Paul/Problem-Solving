class Solution:
    def __init__(self):
        pass
    
    def is_safe(self, i, j, val, board):
        # row
        for k in range(9):
            if board[i][k] == val:
                return False
        # col
        for k in range(9):
            if board[k][j] == val:
                return False

        # grid
        grid_row_start = 3 * (i // 3)
        grid_col_start = 3 * (j // 3)

        for row in range(grid_row_start, grid_row_start + 3):
            for col in range(grid_col_start, grid_col_start + 3):
                if board[row][col] == val:
                    return False

        # If no conflicts, return True
        return True

    def update(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for val in range(1, 10):
                        if self.is_safe(i, j, str(val), board):
                            board[i][j] = str(val)
                            if self.update(board):
                                return True
                            board[i][j] = "."
                    return False  # Trigger backtracking if no valid number can be placed
        return True  # All cells are filled, Sudoku is solved

    def solveSudoku(self, board):
        self.update(board)

# Test Case
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

s = Solution()
s.solveSudoku(board)
print(board)
