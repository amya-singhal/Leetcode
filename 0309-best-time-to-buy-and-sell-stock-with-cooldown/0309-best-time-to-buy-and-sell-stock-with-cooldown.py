class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSoFar = 0
        dp = {}
        def profitCalculator(index, state):
            if index >= len(prices):
                return 0
            if (index, state) in dp:
                return dp[(index, state)]
            if state == 'b':
                profit = max(profitCalculator(index+1, 's') - prices[index], profitCalculator(index+1, 'b'))
                dp[(index, state)] = profit
            else:
                profit = max(profitCalculator(index+2, 'b')+prices[index], profitCalculator(index+1, 's'))
                dp[(index, state)] = profit
            return dp[(index, state)]
        
        profitCalculator(0, 'b')
        return profitCalculator(0, 'b')
                
                