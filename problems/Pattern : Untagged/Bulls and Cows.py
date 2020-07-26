class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b,c,mem1,mem2=0,0,[],[]
        for d1,d2 in zip(secret,guess):
            if d1==d2:
                b+=1
                continue
            mem1.append(d1)
            mem2.append(d2)
        
        common=set(mem1).intersection(mem2)
        m1=Counter(mem1)
        m2=Counter(mem2)
        for cm in common:
            c+=min(m1[cm],m2[cm])
        
        return f"{b}A{c}B"
        
            
            
            