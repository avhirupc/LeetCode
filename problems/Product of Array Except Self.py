class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_product=[1 for i in nums]
        right_product=[1 for i in nums]
        output=[]
        for i in range(1,len(nums)):
            left_product[i]=nums[i-1]*left_product[i-1]
        for i in range(len(nums)-2,-1,-1):
            right_product[i]=nums[i+1]*right_product[i+1]
        return [ left_product[i]*right_product[i]
            for i in range(len(nums))
               ]