class Solution:
    def convertToTitle(self, n: int) -> str:
        map={i+1 : chr(ord('A')+i) for i in range(26)}
        map[0]='Z'
        res=""
        while(n>0):
            res=map[n%26]+res
            if n%26==0:
                n=n-1
            n=n//26
        return res
        
        