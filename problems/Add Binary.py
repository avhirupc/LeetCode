class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        res=""
        aitr=len(a)-1
        bitr=len(b)-1
        while(aitr>=0 and bitr>=0):
            val=(int(a[aitr])+int(b[bitr])+carry)
            dig=val%2
            carry=val//2
            res=str(dig)+res
            aitr-=1
            bitr-=1
        while(aitr>=0):
            val=(int(a[aitr])+carry)
            dig=val%2
            carry=val//2
            res=str(dig)+res
            aitr-=1
        while(bitr>=0):
            val=(int(b[bitr])+carry)
            dig=val%2
            carry=val//2
            res=str(dig)+res
            bitr-=1
        if carry!=0:
            res=str(carry)+res
        return res
            