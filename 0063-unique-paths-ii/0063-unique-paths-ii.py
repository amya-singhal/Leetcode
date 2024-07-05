class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1 for _ in range(col)] for _ in range(row)]
        if obstacleGrid[0][0] == 1:
                return 0
        dp[0][0] = 1
        for i in range(1, col):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i-1]
        for i in range(1, row):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[row-1][col-1]