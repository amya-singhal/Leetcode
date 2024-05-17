class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(x,y):
            if x == m-1 or y == n-1:
                return 1
            elif (x,y) not in dp:
                dp[(x,y)] = dfs(x+1,y)+dfs(x,y+1)
            return dp[(x,y)]
        return dfs(0,0)

        