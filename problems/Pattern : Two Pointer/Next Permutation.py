class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return 
        #find position from last position where increasing digits stops
        index = len(nums)-2
        while(index>=0):
            if nums[index]<nums[index+1]:
                sp=index
                break
            index-=1
        
        #if position not found, already in descending order, so sort and return
        if index==-1:
            nums.sort()
            return 
        
        #find the position from the swap point, which is min amongst the rest still greater than swap point value
        
        sp_val=nums[sp]
        min_pos,min_val=sp+1, nums[sp+1]
        j=sp+1
        
        while(j<len(nums)):
            if nums[j]<min_val and nums[j]>sp_val:
                min_pos=j
                min_val=nums[j]
            j+=1
        
        #swap min_pos to swap point
        nums[sp],nums[min_pos]=nums[min_pos],nums[sp]
        nums[sp+1:]=sorted(nums[sp+1:])
            
            
        
                
            
        