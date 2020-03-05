class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        self.memory=[0]
        for i,n in enumerate(nums):
            if i==0:
                self.memory.append(n)
                continue
            self.memory.append(self.memory[-1]+n)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.memory[j+1]-self.memory[i]
        

