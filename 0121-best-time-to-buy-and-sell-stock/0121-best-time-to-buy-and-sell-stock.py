class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        maxNumber = prices[l-1]
        profit = 0
        for i in reversed(prices):
            if i >= maxNumber:
                maxNumber = i
            else:
                temp = maxNumber - i
                profit = max(temp, profit)
        return profit