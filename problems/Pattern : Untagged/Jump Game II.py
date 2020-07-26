"""On2"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        min_no_of_jump=[float("inf")]*len(nums)
        LP=len(nums)-1
        min_no_of_jump[LP]=0
        for pos in range(len(nums)-2,-1,-1):
            if nums[pos]!=0:
                last_pos=min(pos+nums[pos],LP)
                min_no_of_jump[pos]=min(min_no_of_jump[pos+1:last_pos+1])+1
        return min_no_of_jump[0]
"""On"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        pos=nums[0]
        max_pos_reach_from_current_i=nums[0]
        if len(nums)==1:
            return 0
        jumps=1
        for i in range(1,len(nums)):
            if i>pos:
                jumps+=1
                pos=max_pos_reach_from_current_i
            max_pos_reach_from_current_i=max(max_pos_reach_from_current_i,i+nums[i])
        return jumps