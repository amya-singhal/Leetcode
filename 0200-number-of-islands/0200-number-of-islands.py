class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        numberOfIslands = 0
        
        def dfs(i, j):
            nonlocal directions
            grid[i][j] = '-1'
            for x, y in directions:
                newi, newj = i+x, j+y
                if 0 <= newi < m and 0 <= newj < n and grid[newi][newj] == '1':
                    dfs(newi, newj)
            return
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    numberOfIslands += 1
                    
        return numberOfIslands