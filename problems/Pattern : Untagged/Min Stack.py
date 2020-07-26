from collections import deque
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk=deque([])
        self.min=float("inf")
        

    def push(self, x: int) -> None:
        self.stk.append(x)
        if x<self.min:
            self.min=x

    def pop(self) -> None:
        self.stk.pop()
        if len(self.stk)==0:
            self.min=float("inf")
            return 
        self.min=min(self.stk)
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()