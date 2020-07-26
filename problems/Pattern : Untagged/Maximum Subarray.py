class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return -2147483648
        if len(nums)==1:
            return nums[0]
        memory=[0]*len(nums)
        memory[0]=nums[0]
        for i in range(1,len(nums)):
            memory[i]=max(nums[i],nums[i]+memory[i-1])
        return max(memory)
            
        