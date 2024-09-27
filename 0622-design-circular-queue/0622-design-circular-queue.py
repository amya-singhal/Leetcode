class MyCircularQueue:
    """
      4
      -1  2  3 4 
               f 
          r      
    """
    def __init__(self, k: int):
        self.max_capacity = k
        self.capacity = 0
        self.array = [-1 for _ in range(k)]
        self.f = -1
        self.r = -1
        
    def enQueue(self, value: int) -> bool:
        if self.capacity == self.max_capacity:
            return False
        newf = self.f+1
        if self.f == (self.max_capacity - 1):
            newf = 0
            while self.array[newf] != -1:
                newf += 1
        self.array[newf] = value
        self.f = newf
        if self.capacity == 0:
            self.r = 0
        self.capacity += 1
        return True
        
    def deQueue(self) -> bool:
        # print(self.array, self.f, self.r)
        if self.isEmpty():
            return False
        self.array[self.r] = -1
        self.capacity -= 1
        if self.capacity > 0:
            newr = self.r+1
            if self.r == (self.max_capacity-1):
                newr = 0
                while self.array[newr] == -1:
                    newr += 1
            self.r = newr
        if self.capacity == 0:
            self.r, self.f = -1, -1
        return True
        
    def Front(self) -> int:
        # print(self.array, self.r)
        return self.array[self.r]

    def Rear(self) -> int:
        return self.array[self.f]

    def isEmpty(self) -> bool:
        return not self.capacity
        
    def isFull(self) -> bool:
        return self.capacity == self.max_capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()