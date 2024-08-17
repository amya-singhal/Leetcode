class StockSpanner:

    def __init__(self):
        self.stack = []
        # [(100,1), (85,6)]

    def next(self, price: int) -> int:
        stack = self.stack
        span = 1
        while stack and stack[-1][0] <= price:
            lastPrice, lastSpan = stack.pop()
            span += lastSpan
        stack.append((price, span))
        return span
        
        
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)