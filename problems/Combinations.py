class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        solutions=[]
        prefix=[]
        candidates=list(range(1,n+1))
        for pos in range(n):
            self.combineUtil(
                pos,
                k-1,
                candidates,
                prefix+[candidates[pos]],
                solutions
            )
        return solutions
    
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
        