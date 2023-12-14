class MinStack:

    def __init__(self):
        self.ls=[]
        self.minls=[]
        

    def push(self, val: int) -> None:
        self.ls.append(val)
        if self.minls:
            val = min(self.minls[-1],val)
        self.minls.append(val)
        

    def pop(self) -> None:
        self.ls.pop()
        self.minls.pop()
        

    def top(self) -> int:
        return self.ls[-1]
        

    def getMin(self) -> int:
        return self.minls[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()