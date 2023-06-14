class TimeMap:

    def __init__(self):
        self.ans = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ans:
            self.ans[key] = [[value, timestamp]]
        else:
            self.ans[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        s = ""
        values = []
        if key in self.ans:
            values = self.ans[key]
        if not values:
            return ""
        l = 0
        h = len(values) - 1
        while(l <= h):
            m = (l+h)//2
            if values[m][1] == timestamp:
                s = values[m][0]
                break
            elif values[m][1] > timestamp:
                h = m - 1
            else:
                s = values[m][0]
                l = m + 1
        return s
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)