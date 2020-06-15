class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort nums
        # fix one element and iterate
        # fix second element and iterate
        min_dtz =float("inf")
        ans=None
        nums=sorted(nums)
        for ind_i in range(len(nums)-2):
            C = nums[ind_i] - target
            lptr,rptr=ind_i+1,len(nums)-1
            while(lptr < rptr):
                dtz=nums[lptr]+nums[rptr]+C
                dtz_abs=abs(dtz)
                if min_dtz> dtz_abs:
                    min_dtz=dtz_abs
                    ans=dtz+target
                if dtz>0:
                    rptr-=1
                    continue
                lptr+=1
        return ans
        