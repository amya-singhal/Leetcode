class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices))]
        maxx = float('-inf')
        for i in range(1, len(prices)):
            subMax = dp[i-3] if i-3 >= 0 else 0
            maxx = max(maxx, subMax - prices[i-1])
            dp[i] = max(dp[i-1], maxx+prices[i])
        
        return dp[-1]
                