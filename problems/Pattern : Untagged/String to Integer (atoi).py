class Solution:
    def myAtoi(self, str: str) -> int:
        st=0
        while(st<len(str) and str[st]==" "):
            st+=1
        en=st+1
        digits=["0","1","2","3","4","5","6","7","8","9"]
        while(en<len(str) and str[en] in digits):
            en+=1
        try:
            res=int(str[st:en])
        except:
            res=0
        if res<-2147483648:
            return -2147483648
        if res>2147483647:
            return 2147483647
        return res
        