class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        word = "ABCCED"
        """
        n = len(board)
        m = len(board[0])
        visited = set()
        def dfs(i,j, index):
            if index == len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[index] or (i,j) in visited:
                return False
            visited.add((i,j))
            res = (dfs(i+1, j, index+1) or dfs(i-1,j,index+1) or dfs(i,j+1, index+1) or dfs(i,j-1,index+1))
            visited.remove((i,j))
            return res
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False