class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1 for _ in range(k)]
        self.limit = 0
        self.rear = -1
        self.front = -1
        self.max_limit = k
        # [0,1,2,3,4,0,0]
        #    f     r
    def enQueue(self, value: int) -> bool:
        if self.max_limit == self.limit:
            return False
        newPlace = self.rear+1
        if self.rear == self.max_limit-1:
            newPlace = 0
            while (self.queue[newPlace] != -1):
                newPlace += 1
        if self.limit == 0:
            self.front = 0
        self.rear = newPlace
        self.queue[self.rear] = value
        self.limit += 1
        # print(self.queue, self.front, self.rear)
        return True

    def deQueue(self) -> bool:
        if self.limit == 0:
            return False
        self.queue[self.front] = -1
        self.limit -= 1
        if self.limit > 0:
            newFront = self.front + 1
            if self.front == self.max_limit-1:
                newFront = 0
                while self.queue[newFront] == -1:
                    newFront += 1
            self.front = newFront
        else:
            self.front, self.rear = -1,-1
        # print(self.queue, self.front, self.rear)
        return True
            
        
    def Front(self) -> int:
        return self.queue[self.front]

    def Rear(self) -> int:
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.limit == 0
        
    def isFull(self) -> bool:
        return self.limit == self.max_limit


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()