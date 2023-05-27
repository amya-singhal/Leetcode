class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(len(self.minVal) == 0):
            self.minVal.append(val)
        elif (self.minVal[-1] >= val):
            self.minVal.append(val)
        

    def pop(self) -> None:
        if (self.stack[-1] == self.minVal[-1]):
            del self. minVal[-1]
        del self.stack[-1]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()