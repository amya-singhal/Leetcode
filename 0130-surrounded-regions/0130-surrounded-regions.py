class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rL, cL = len(board), len(board[0])
        # dfs method
        def dfs(r, c):
            if (r < 0 or c < 0 or r == rL or c == cL or board[r][c] != "O"):
                return
            board[r][c] = "V"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # going through the boards of the board to implement dfs on 'O'
        for i in range(rL):
            for j in range(cL):
                if (board[i][j] == "O" and ((i in [0, rL - 1]) or (j in [0, cL - 1]))):
                    dfs(i, j)
        # change values
        for i in range(rL):
            for j in range(cL):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'V':
                    board[i][j] = 'O'        
        
        
        """
        Do not return anything, modify board in-place instead.
        """
        