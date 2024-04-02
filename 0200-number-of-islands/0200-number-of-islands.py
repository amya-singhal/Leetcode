class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(i, j):
            nonlocal grid, directions
            for x,y in directions:
                newx, newy = x+i, y+j
                if 0 <= newx < n and 0 <= newy < m and grid[newx][newy] == '1':
                    grid[newx][newy] = '2'
                    dfs(newx, newy)
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans
        
        