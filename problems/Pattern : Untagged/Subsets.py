class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solutions=[]
        prefix=[]
        candidates=nums
        for k in range(0,len(nums)+1):
            for pos in range(len(nums)):
                self.combineUtil(
                    pos,
                    k-1,
                    candidates,
                    prefix+[candidates[pos]],
                    solutions
                )
        return [[]]+solutions
    
    def combineUtil(self,pos,k,candidates,prefix,solutions):
        if k==0:
            solutions.append(prefix)
            return
        for next_pos in range(pos+1,len(candidates)):
            self.combineUtil(
                next_pos,
                k-1,
                candidates,
                prefix+[candidates[next_pos]],
                solutions
            )
    