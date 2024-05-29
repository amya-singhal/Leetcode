class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        m = len(grid)
        n = len(grid[0])
        visited = []
        count = 0
        q = [] 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 and (i,j) not in visited:
                    q.append((i,j, 0))
                    
        while q:
            l = len(q)
            for _ in range(l):
                x,y, level = q.pop(0)
                visited.append((i,j))
                for i,j in d:
                    newx, newy = x+i, y+j
                    if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == 1:
                        count = max(count, level+1)
                        grid[newx][newy] = 2
                        q.append((newx, newy, level+1))
            
                        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return count