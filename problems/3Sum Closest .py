"""Wrong Submission Two test"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        _min=float("inf")
        _min_set=[]
        itr=0
        while(itr<len(nums)-2):
            st=itr+1
            en=len(nums)-1
            while(st<en):
                if _min>abs(target-(nums[itr]+nums[st]+nums[en])):
                    _min_set=[nums[itr],nums[st],nums[en]]
                    _min=abs(target-(nums[itr]+nums[st]+nums[en]))
                #kisase chota distance aa rha h 
                if abs(target-(nums[itr]+nums[st+1]+nums[en]))>abs(target-(nums[itr]+nums[st]+nums[en-1])):
                    en-=1
                else:
                    st+=1
            itr+=1
        return sum(_min_set)
                
            
            
        