class StockPrice:

    def __init__(self):
        self.stockPrices = {}
        self.currentTimestamp = None
        self.currentPrice= None
        self.maxi = []
        self.mini = []

    def update(self, timestamp: int, price: int) -> None:
        self.stockPrices[timestamp] = price
        heapq.heappush(self.maxi, (-1*price, timestamp))
        heapq.heappush(self.mini, (price, timestamp))
        
        if not self.currentTimestamp or timestamp >= self.currentTimestamp:
            self.currentTimestamp = timestamp
            self.currentPrice = price

    def current(self) -> int:
        return self.currentPrice

    def maximum(self) -> int:
        maxprice, maxtimestamp = self.maxi[0]
        while self.stockPrices[maxtimestamp] != -1*maxprice:
            heapq.heappop(self.maxi)
            maxprice, maxtimestamp = self.maxi[0]
        return -1*maxprice

    def minimum(self) -> int:
        miniprice, minitimestamp = self.mini[0]
        while self.stockPrices[minitimestamp] != miniprice:
            heapq.heappop(self.mini)
            miniprice, minitimestamp = self.mini[0]
        return miniprice


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()