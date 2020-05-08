
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stk=[]        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stk.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp=[]
        while(len(self.stk)!=1):
            v=self.stk.pop()
            tmp.append(v)
        res=self.stk.pop()
        for v in tmp[::-1]:
            self.stk.append(v)
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        tmp=[]
        while(len(self.stk)!=0):
            v=self.stk.pop()
            tmp.append(v)
        res=tmp[-1]
        for v in tmp[::-1]:
            self.stk.append(v)
        return res

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stk)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()