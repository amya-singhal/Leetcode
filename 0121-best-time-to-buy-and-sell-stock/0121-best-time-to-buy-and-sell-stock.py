class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = prices[0]
        for price in prices:
            p = price - mini
            profit = max(profit, p)
            mini = min(mini, price)
        return profit