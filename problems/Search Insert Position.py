class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.find_pos(nums,0,len(nums)-1,target)
        
    def find_pos(self,nums,st,en,target):
        #if not found
        if st>en:
            return st
        mid=(st+en)//2
        #if found
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return self.find_pos(nums,st,mid-1,target)
        
        return self.find_pos(nums,mid+1,en,target)
        
        
        