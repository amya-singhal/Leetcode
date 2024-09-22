class LFUCache:

    def __init__(self, capacity: int):
        self.hashMap = defaultdict(OrderedDict)
        self.capacity = capacity
        self.keysFreq = defaultdict()
        self.minFreq = 0

    def updateFreq(self, key: int, value: int) -> int:
        freq = self.keysFreq[key]
        val = self.hashMap[freq].pop(key)
        if value:
            val = value
        self.keysFreq[key] += 1
        self.hashMap[freq+1][key] = val
        if self.minFreq == freq and not self.hashMap[freq]:
            self.minFreq += 1
        # print(self.hashMap)
        return val
        
    def get(self, key: int) -> int:
        if key not in self.keysFreq:
            return -1
        # print(self.updateFreq(key, None))
        return self.updateFreq(key, None)
            

    def put(self, key: int, value: int) -> None:
        if key in self.keysFreq:
            self.updateFreq(key, value)
        
        else:
            if self.capacity == len(self.keysFreq):
                self.keysFreq.pop(
                    self.hashMap[self.minFreq].popitem(last=False)[0])
            self.keysFreq[key] = 1
            self.hashMap[1][key] = value
            self.minFreq = 1
        # print(self.keysFreq)
            
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)