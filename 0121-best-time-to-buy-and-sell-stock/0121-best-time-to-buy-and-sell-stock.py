class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l < 2:
            return 0
        minN = prices[0]
        maxP = 0
        for p in prices[1:]:
            maxP = max(maxP, p-minN)
            minN = min(minN, p)
        return maxP
            