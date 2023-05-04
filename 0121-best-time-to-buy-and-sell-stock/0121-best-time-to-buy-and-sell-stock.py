class Solution(object):
    def maxProfit(self, prices):
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
        
        """
        :type prices: List[int]
        :rtype: int
        """
        