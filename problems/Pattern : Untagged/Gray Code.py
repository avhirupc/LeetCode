class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n==0:
            return [0]
        traversed=set([])
        sequence=[]
        code="0"*n
        self.dfs(code,traversed,sequence)
        return sequence
    
    def dfs(self,code,traversed,sequence):
        if code in traversed:
            return
        sequence.append(int(code,2))
        traversed.add(code)
        for pos in range(len(code)-1,-1,-1):
            if code[pos]=="1":
                continue
            self.dfs(
                code[:pos]+"1"+code[pos+1:],
                traversed,
                sequence)
        return
    
        