class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        nums=sorted(nums,reverse=True)
        sum_,itr=0,0
        while(itr<len(nums)):
            sum_+=nums[itr]
            if sum_> total-sum_:
                return nums[:itr+1]
            itr+=1
            
            
        
        