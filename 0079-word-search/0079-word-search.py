class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        first = word[0]
        n = len(board)
        m = len(board[0])
        s = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(i, j, start, visited) -> bool:
            # print(board[i][j], i, j, start)
            visited.add((i, j))
            nonlocal directions
            if start == len(word)-1:
                return True
            for x, y in directions:
                newx = i + x
                newy = j + y
                if 0<=newx<n and 0<=newy<m and board[newx][newy] == word[start+1] and (newx, newy) not in visited and dfs(newx, newy, start+1, visited.copy()):
                    return True
            return False
        for i in range(n):
            for j in range(m):
                if board[i][j] == first:
                    # print(i, j)
                    visited = set()
                    if dfs(i, j, 0, visited) == True:
                        return True
        return False