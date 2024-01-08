class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(len(p)+1)] for _ in range(0, len(s)+1)]
        dp[len(s)][len(p)] = True
        for i in range(len(p)-1, -1, -1):
            if p[i] == '*':
                dp[len(s)][i] = dp[len(s)][i+1]
        for i in range(len(s)-1, -1, -1):
            for j in range(len(p)-1, -1, -1):
                if p[j] == '?' or p[j] == s[i]:
                    dp[i][j] = dp[i+1][j+1]
                elif p[j] == '*':
                    dp[i][j] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j+1]
        return dp[0][0]