class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nh=len(nums)
        memory=[0]*(nh)
        if nh==0:
            return 0
        memory[0]=nums[0]
        if nh==1:
            return memory[0]
        memory[1]=max(nums[0],nums[1])
        if nh==2:
            return memory[1]
        for i in range(2,nh):
            memory[i]=max(nums[i]+memory[i-2],memory[i-1])
        return memory[nh-1]
        