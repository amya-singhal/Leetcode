class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        word = "ABCCED"
        """
        n = len(board)
        m = len(board[0])
        def dfs(i,j, index, visited):
            visited.append([i,j])
            if index == len(word):
                return True
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for x,y in directions:
                if 0 <= i+x < n and 0 <= j+y < m and board[i+x][j+y] == word[index] and [i+x,j+y] not in visited:
                    if dfs(i+x, j+y, index + 1, visited.copy()):
                        return True
            return False
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    print(i, j)
                    if dfs(i, j, 1, []):
                        return True
        return False