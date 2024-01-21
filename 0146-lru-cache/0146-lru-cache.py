class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = defaultdict(int)  

    def get(self, key: int) -> int:
        if key in self.d:
            val = self.d[key]
            del self.d[key]
            self.d[key] = val
            return self.d[key]
        return -1    

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
            self.d[key] = value
        elif len(self.d) == self.capacity:
            del self.d[next(iter(self.d))]
            self.d[key] = value
        else:
            self.d[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)