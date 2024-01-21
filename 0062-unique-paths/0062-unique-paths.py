class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = set()
        dp = {}
        def dfs(i,j):
            if i == m-1 or j == n-1:
                return 1
            elif (i,j) not in dp:
                dp[(i,j)] = dfs(i+1,j) + dfs(i, j+1)
            return dp[(i,j)]
        return dfs(0,0)
