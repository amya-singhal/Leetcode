class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        past = prices[0]
        tmp = 0
        for i in prices:
            if i < past:
                past = i
                profit += tmp
                tmp = 0
            elif i > past:
                tmp += i - past
                past = i
        return profit+tmp