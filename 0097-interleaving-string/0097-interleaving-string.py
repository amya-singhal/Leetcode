class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ls1 = len(s1)
        ls2 = len(s2)
        ls3 = len(s3)
        if ls1 + ls2 != ls3:
            return False
        dp = [[False] * (ls1+1) for _ in range(ls2+1)]
        dp[0][0] = True
        for i in range(1, ls2+1):
            dp[i][0] = dp[i-1][0] and s2[i-1] == s3[i-1]
        for i in range(1, ls1+1):
            dp[0][i] = dp[0][i-1] and s1[i-1] == s3[i-1]
        for i in range(1, ls2+1):
            for j in range(1, ls1+1):
                dp[i][j] = (dp[i-1][j] and s2[i-1] == s3[i-1+j]) or (dp[i][j-1] and s1[j-1] == s3[i-1+j])
        return dp[ls2][ls1]