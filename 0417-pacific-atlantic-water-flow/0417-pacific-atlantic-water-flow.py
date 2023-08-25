class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visit, prevH):
            if (r,c) in visit or r<0 or c<0 or r>=n or c>=m or heights[r][c] < prevH:
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        for r in range(n):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, m-1, atlantic, heights[r][m-1])
        for c in range(m):
            dfs(0, c, pacific, heights[0][c])
            dfs(n-1, c, atlantic, heights[n-1][c])
        ans = []
        for i in range(n):
            for j in range(m):
                if (i,j) in pacific and (i,j) in atlantic:
                    ans.append([i, j])
        return ans
                    
            