#wrong solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        st=0
        en=len(nums)
        if en==0:
            return [-1,-1]
        if en==1:
            return [0,0] if nums[0]==target else [-1,-1]
        en=en-1
        return self.searchRangeUtil(nums,st,en,target)
    
    def searchRangeUtil(self,nums: List[int], st:int, en:int,target:int)-> List[int]:
        if st>en or en==-1 or en==len(nums):
            return [-1,-1]
        mid=(st+en)//2
        print(mid)
        if nums[mid]==target:
            #find first occurence and last occurence
            st_ind,en_ind=mid-1,mid+1
            while(nums[st_ind]==target):
                st_ind-=1
            while(nums[en_ind]==target):
                en_ind+=1
            return [st_ind+1,en_ind-1]
        if nums[mid]>target:
            return self.searchRangeUtil(nums,st,mid-1,target)
        else:
            return self.searchRangeUtil(nums,mid+1,en,target)
        