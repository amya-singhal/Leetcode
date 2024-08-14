class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices))]
        
        for i in range(1, len(prices)):
            dp[i] = dp[i-1]
            for j in range(i):
                subMax = dp[j-2] if j >= 2 else 0
                dp[i] = max(dp[i], subMax+ prices[i] - prices[j])
        
        return max(dp)
                