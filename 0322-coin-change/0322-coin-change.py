class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        if amount == 0:
            return 0
        for i in range(amount+1):
            for coin in coins:
                if i == coin:
                    dp[i] = 1
                elif coin < i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]