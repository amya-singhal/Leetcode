class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[float("inf")]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for x,y,t in edges:
            dp[x][y] = t
            dp[y][x] = t
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
        d = {}
        for i in range(n):
            c = 0
            for j in range(n):
                if dp[i][j] <= distanceThreshold and i != j:
                    c += 1
            d[i] = c
        
        x = min(d.values())
        maxi = 0
        for k,v in d.items():
            if x == v:
                maxi = max(maxi, k)
        return maxi
            