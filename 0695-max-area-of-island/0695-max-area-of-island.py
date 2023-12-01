class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(i, j, area):
            grid[i][j] = 2
            for (x,y) in directions:
                newI = x+i
                newJ = y+j
                if (0 <= newI < n and 0 <= newJ < m and grid[newI][newJ] == 1):
                    area = bfs(newI, newJ, area+1)
            return area
            
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if (grid[i][j] == 1):
                    area = bfs(i, j, 1)
                    maxArea = max(maxArea, area)
        return maxArea