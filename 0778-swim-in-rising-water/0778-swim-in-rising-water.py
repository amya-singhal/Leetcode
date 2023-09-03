class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        h = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0,0))
        t = 0
        while(True):
            mini, nextx, nexty = heappop(h)
            t = max(t, mini)
            if nextx == n-1 and nexty == m-1:
                return t
            for x,y in directions:
                newx = nextx+x
                newy = nexty+y
                if 0<=newx<n and 0<=newy<m and (newx, newy) not in visited:
                    visited.add((newx,newy))
                    heappush(h, (grid[newx][newy], newx, newy))
        return t