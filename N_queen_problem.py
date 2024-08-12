class Solution:
    def is_safe(self, i, j, board, n):
        # same row
        for col in range(n):
            if board[i][col] == "Q":
                return False
        # same col
        for row in range(n):
            if board[row][j] == "Q":
                return False
        # upper left diagonal
        r = i
        c = j
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        # upper right diagonal
        r = i
        c = j
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
        # lower left diagonal
        r = i
        c = j
        while r < n and c >= 0:
            if board[r][c] == "Q":
                return False
            r += 1
            c -= 1
        # lower right diagonal
        r = i
        c = j
        while r < n and c < n:
            if board[r][c] == "Q":
                return False
            r += 1
            c += 1
        return True

    def compute_result(self, i, board, res, n):
        if i == n:
            res.append(["".join(row) for row in board])
            return
        for j in range(n):
            if self.is_safe(i, j, board, n):
                board[i][j] = "Q"
                self.compute_result(i + 1, board, res, n)
                board[i][j] = "."

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        for i in range(n):
            board[0][i] = "Q"
            self.compute_result(1, board, res, n)
            board[0][i] = "."
        return res
