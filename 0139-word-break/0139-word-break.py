class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tmp = ""
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        l = 0
        for i in range(len(s)+1):
            if dp[i]:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        dp[i+len(word)] = dp[i]
        print(dp)
        return dp[len(s)]