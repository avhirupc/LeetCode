class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        itr=0
        
        while(itr!=len(nums)):
            if nums[itr]==val:
                del nums[itr]
            else:
                itr+=1
                
        return len(nums)
        