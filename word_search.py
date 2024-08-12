class Solution:
    def is_safe(self, i, j, visit):
        if i < 0 or i >= len(visit):
            return False
        if j < 0 or j >= len(visit[0]):
            return False
        if visit[i][j] == True:
            return False
        return True

    def dfs(self, i, j, idx, visit, board, word):
        # print(i, j, idx)
        if idx >= len(word):
            return True
        if board[i][j] != word[idx]:
            return False
        visit[i][j] = True
        # top
        if self.is_safe(i - 1, j, visit):
            if self.dfs(i - 1, j, idx + 1, visit, board, word):
                return True
        # bottom
        if self.is_safe(i + 1, j, visit):
            if self.dfs(i + 1, j, idx + 1, visit, board, word):
                return True
        # left
        if self.is_safe(i, j - 1, visit):
            if self.dfs(i, j - 1, idx + 1, visit, board, word):
                return True
        # right
        if self.is_safe(i, j + 1, visit):
            if self.dfs(i, j + 1, idx + 1, visit, board, word):
                return True
        visit[i][j] = False
        if idx == len(word) - 1: #for handling the (1,1) length board
            return True
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if visit[i][j] == False:
                    if self.dfs(i, j, 0, visit, board, word):
                        return True
        return False
