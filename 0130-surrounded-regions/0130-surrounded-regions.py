class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # to solve it run dfs
        # first we find the first 0 and continue dfs on that
        n = len(board)
        m = len(board[0])
        def dfs(x,y):
            nonlocal board
            if x < 0 or y < 0 or x == n or y == m or board[x][y] != "O":
                return
            # print("here")
            board[x][y] = "T"
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x, y+1)
            dfs(x, y-1)
             
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and ((i in [0, n-1]) or (j in [0, m-1])):
                    dfs(i,j)
        # print(board)
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"
        
                    
                    
        """
        Do not return anything, modify board in-place instead.
        """
        