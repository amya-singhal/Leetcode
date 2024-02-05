class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        ans = []
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        atlantic, pacific = False, False
        def check(i, j, visited):
            nonlocal pacific, atlantic
            visited.add((i, j))
            if i == n-1 or j == m-1:
                    atlantic = True
            if i == 0 or j == 0:
                    pacific = True
            for x, y in directions:
                newx, newy = x+i, y+j
                if 0 <= newx < n and 0 <= newy < m and heights[newx][newy] <= heights[i][j] and (newx, newy) not in visited:
                    check(newx, newy, visited)
        
        for i in range(n):
            for j in range(m):
                atlantic, pacific = False, False
                check(i, j, set())
                if pacific and atlantic:
                    ans.append([i,j])
        return ans
                    
        