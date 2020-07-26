class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos_jump=[0]*(len(nums)+1)
        max_pos_jump[len(nums)]=len(nums)
        for pos,val in list(enumerate(nums))[::-1]:
            if val!=0:
                end_pos=min(pos+val,len(nums)+2)
                max_pos_jump[pos]=max(max_pos_jump[pos+1:end_pos+1])
            else:
                max_pos_jump[pos]=pos
        return max_pos_jump[0]>=len(nums)-1
        