from bisect import bisect_left
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mem=[]
        self.len=0
        

    def addNum(self, num: int) -> None:
        # pos=0
        # for pos in range(self.len+1):
        #     if pos==self.len:
        #         break
        #     if num < self.mem[pos]:
        #         break
        pos=bisect_left(self.mem,num)
        self.mem.insert(pos,num)
        self.len+=1

    def findMedian(self) -> float:
        if self.len%2!=0:
            return self.mem[self.len//2]
        mid=self.len//2
        return (self.mem[mid]+self.mem[mid-1])/2
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()