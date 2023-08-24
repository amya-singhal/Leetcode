class MedianFinder:

    def __init__(self):
        self.mini = []
        self.maxi = []
        

    def addNum(self, num: int) -> None:
        heappush(self.mini, -num)
        # print(self.mini, self.maxi)
        if self.mini and self.maxi and (-self.mini[0] > self.maxi[0]):
            x = heappop(self.mini)
            heappush(self.maxi, -x)     
        if len(self.mini) - len(self.maxi) > 1:
            x = heappop(self.mini)
            heappush(self.maxi, -x)
        if len(self.maxi) - len(self.mini) > 1:
            x = heappop(self.maxi)
            heappush(self.mini, -x)
        # print(self.mini, self.maxi)
        

    def findMedian(self) -> float:
        # print(self.mini, self.maxi)
        if len(self.mini) == len(self.maxi):
            x,y = -self.mini[0],self.maxi[0]
            return (x+y)/2
        elif len(self.mini) > len(self.maxi):
            return -self.mini[0]
        else:
            return self.maxi[0]
            
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()