class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        s = ""
        x = []
        if key in self.d:
            x = self.d[key]
        if not x:
            return ""
        l = 0
        r = len(x)-1
        while(l <= r):
            m = (l+r) // 2
            if x[m][1] == timestamp:
                s = x[m][0]
                break
            elif x[m][1] > timestamp:
                r = m-1
            else:
                s = x[l][0]
                l = m+1
        return s
                
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)