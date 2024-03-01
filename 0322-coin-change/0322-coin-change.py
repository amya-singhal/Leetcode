class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        coins = [1,2,5], amount = 11
        dp = [0,1,0,0,0,0,0,0,0,0]
        
        """
        ans = float('inf')
        dp = [(amount+1) for _ in range(amount+1)]
        dp[0] = 0
        for a in range(1, len(dp)):
            for coin in coins:
                if a == coin:
                    dp[a] = 1
                elif 0 <= a-coin:
                    dp[a] = min(dp[a-coin]+1, dp[a])
        if dp[-1] >= amount+1:
            return -1
        return dp[-1]