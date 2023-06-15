class MinStack:

    def __init__(self):
        self.s =[]
        self.minV = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.minV) == 0:
            self.minV.append(val)
        elif self.minV[-1] >= val:
            self.minV.append(val)
        

    def pop(self) -> None:
        if self.s[-1] == self.minV[-1]:
            self.minV.pop(-1)
        self.s.pop(-1)
        

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minV[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()