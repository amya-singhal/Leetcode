class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        d = self.d
        heapq.heappush(d[key], (timestamp, value))
        # -1,-2             

    def get(self, key: str, timestamp: int) -> str:
        x = self.d[key]
        # print(self.d)
        if len(x) == 0:
            return ""
        tmp = []
        while x:
            t, v = x.pop()
            if t > timestamp:
                tmp.append((t,v))
            else:
                # print(t,v)
                tmp.append((t,v))
                for i,j in tmp:
                    heapq.heappush(x, (i,j))
                return v
        for i,j in tmp:
            heapq.heappush(x, (i,j))
        return ""
            
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)