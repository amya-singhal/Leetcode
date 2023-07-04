class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l = 0
        r = 1
        maxP = 0
        while(r < len(prices)):
            if prices[l] >= prices[r]:
                l = r
            else:
                maxP = max(maxP, prices[r]-prices[l])
            r += 1
        return maxP