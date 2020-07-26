class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        for itr_i in range(len(nums)-3):
            for itr_j in range(itr_i+1,len(nums)-2):
                if ((itr_i!=0 and nums[itr_i]==nums[itr_i-1]) or ( itr_j!=1 and nums[itr_j]==nums[itr_j-1])) and nums[itr_i]!=nums[itr_j]:
                    continue
                C=nums[itr_i]+nums[itr_j]-target
                self.twoSum(nums,C,itr_i,itr_j,res)
        return res
    
    def twoSum(self,nums,C,itr_i,itr_j,res):
        lptr,rptr=itr_j+1,len(nums)-1
        while(lptr<rptr):
            if C+nums[lptr]+nums[rptr]==0:
                res.append([
                    nums[itr_i],
                    nums[itr_j],
                    nums[lptr],
                    nums[rptr]
                ])
            if C+nums[lptr]+nums[rptr]>0:
                while(lptr<rptr and nums[rptr]==nums[rptr-1]):
                    rptr-=1
                rptr-=1
            else:
                while(lptr< rptr and nums[lptr]==nums[lptr+1]):
                    lptr+=1
                lptr+=1
