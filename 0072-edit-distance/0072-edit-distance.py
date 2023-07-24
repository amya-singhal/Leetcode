class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[float("inf")]*(l2+1) for _ in range(l1+1)]
        # 0,0 = 0 0,i = i i,0 = i
        for i in range(l1+1):
            dp[i][l2] = l1 - i
        for j in range(l2+1):
            dp[l1][j] = l2 - j
        for i in range(l1-1, -1,-1):
            for j in range(l2-1, -1,-1):
                # print(i, j)
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]    