class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = prices[0]
        i = 0
        while i < len(prices):
            mini = prices[i]
            p = 0
            while i+1 < len(prices) and prices[i+1] < mini:
                i += 1
                mini = prices[i]
            tmp = mini
            while i+1 < len(prices) and prices[i+1] > mini:
                p = max(p, prices[i+1] - tmp)
                i += 1
                mini = prices[i]
            profit += p
            i += 1
        return profit
    