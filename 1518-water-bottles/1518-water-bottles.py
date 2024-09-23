class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        numBottles = 15, numExchange = 4
        0 -> new filled bottles
        6 -> empty ones
        1 -> filled
        3 -> e
        15 + 3 + 1 -> 19
        """
        filled = 0 # 15
        empty = numBottles # 15
        total = numBottles
        while empty >= numExchange:
            filled = empty // numExchange
            empty = empty % numExchange
            total += filled
            empty += filled
        
        return total